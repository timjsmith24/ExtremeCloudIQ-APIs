import requests

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/iot/:disable"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
