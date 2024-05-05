import logging

import httpx

headers = {"X-Skyfi-Api-Key": "be853cd1a0be4fdb9e4ccef730e22172"}

ping_response = httpx.get("https://app.skyfi.com/platform-api/ping", headers=headers)
ping = ping_response.json()
print(ping)
logging.info(f"ping: {ping['message']}")
