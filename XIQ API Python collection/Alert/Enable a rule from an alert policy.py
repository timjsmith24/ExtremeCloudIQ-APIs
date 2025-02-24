import requests
         
alert_policy_id = 'Alert Policy ID'
alert_rule_id = 'Alert Rule ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-policies/{alert_policy_id}/rules/{alert_rule_id}/:enable"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}



response = requests.post(url, headers=headers, params=params)

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
