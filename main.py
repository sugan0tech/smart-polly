from urllib import response
import requests

url = "https://storage.bunnycdn.com/storageZoneName/path/fileName"

headers = {"Content-Type": "application/octet-stream"}

response = requests.put(url, headers=headers)

print(response.text)