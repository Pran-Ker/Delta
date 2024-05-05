import logging

import httpx
                 
headers = {"X-Skyfi-Api-Key": "be853cd1a0be4fdb9e4ccef730e22172"}


request = {
    "aoi": (
        "POLYGON((-75.30257496772279 -14.579684184450173,-74.93310578102702 -14.572732064728868,"
        "-74.93012696417887 -14.816429192248364,-75.30428913596941 -14.815716491089375,"
        "-75.30257496772279 -14.579684184450173))"
    ),
    "maxCloudCoveragePercent": 0,
    "maxOffNadirAngle": 4,
    "resolutions": ["VERY HIGH"],
    "pageNumber": 0,
    "pageSize": 20,
    "deliveryDriver": "S3",
    "deliveryParams": {
  "s3_bucket_id": "yellow-pad",
  "aws_region": "us-east-1",
  "aws_access_key": "X6SweU3wGDtm9XW7HTPwvB+4+YAHH4KXCc4wFete",
  "aws_secret_key": "AKIAZI2LIGF6JEVCNXZM"
}
}

archives_response = httpx.post(
    "https://app.skyfi.com/platform-api/archives", json=request, headers=headers
)
archives = archives_response.json()

print(archives)

logging.info(f"total results: {archives['total']}")
for archive in archives["archives"]:
    logging.info(f"archive id: {archive['archiveId']}")
