from skimage.metrics import structural_similarity
import cv2
import numpy as np

# Load images
before = cv2.imread('r1.png')
after = cv2.imread('r2.png')

# Convert images to grayscale
before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# Compute SSIM between the two images
(score, diff) = structural_similarity(before_gray, after_gray, full=True)
print("Image Similarity: {:.4f}%".format(score * 100))

# Convert the diff image to 8-bit unsigned integers
diff = (diff * 255).astype("uint8")
diff_box = cv2.merge([diff, diff, diff])

# Threshold and find contours
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros(before.shape, dtype='uint8')
filled_after = after.copy()

# Highlight differences
for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.drawContours(mask, [c], 0, (255, 255, 255), -1)
        cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)

# Display images using cv2.imshow
cv2.imshow('Before', before)
cv2.imshow('After', after)
# cv2.imshow('Diff', diff)
# cv2.imshow('Diff Box', diff_box)
# cv2.imshow('Mask', mask)
# cv2.imshow('Filled After', filled_after)
cv2.waitKey(0)
cv2.destroyAllWindows()
