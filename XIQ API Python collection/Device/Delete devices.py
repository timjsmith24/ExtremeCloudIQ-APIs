import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/:delete?force_delete=false"

payload = json.dumps({
  "ids": [
    0 # List of Device IDs to delete
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
