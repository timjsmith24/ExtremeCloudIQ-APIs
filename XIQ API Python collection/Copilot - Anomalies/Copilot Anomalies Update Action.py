import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/anomalies/update-action"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "anomaly_type": "POE_FLAPPING",
  "action_type": "MUTE",
  "building_id": 0
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
