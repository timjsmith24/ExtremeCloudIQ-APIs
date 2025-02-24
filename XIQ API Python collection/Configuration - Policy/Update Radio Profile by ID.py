import requests
         
radio_profile_id = 'Radio Profile ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/{radio_profile_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "transmission_power": 20,
  "max_transmit_power": 20,
  "transmission_power_floor": 20,
  "transmission_power_max_drop": 18,
  "max_clients": 255,
  "enable_client_transmission_power": True,
  "client_transmission_power": 20,
  "radio_mode": "B_G",
  "enable_ofdma": True
}


response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
