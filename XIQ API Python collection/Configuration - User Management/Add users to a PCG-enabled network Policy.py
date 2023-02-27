import requests
import json

np_id = 0 # Network Policy ID
access_token = '***'

url = f"https://api.extremecloudiq.com/pcgs/key-based/network-policy-{np_id}/users"

payload = json.dumps({
  "users": [
    {
      "name": "string",
      "email": "string",
      "user_group_name": "string"
    }
  ]
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
