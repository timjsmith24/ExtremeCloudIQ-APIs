import requests
         
baseUrl = 'https://api.extremecloudiq.com'
uid = 'admin User ID'
access_token = '***'

url = f"{baseUrl}/users/{uid}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "login_name": "string",
  "display_name": "string",
  "idle_timeout": 0,
  "user_role": "ADMINISTRATOR",
  "location_ids": [
    0
  ],
  "access_scope": 0,
  "viq_access_control": 0
}


response = requests.patch(url, headers=headers, params=params)

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
