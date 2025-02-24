import requests
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt) 
    return int(dt_timezone.timestamp()*1000) # epoch time in milliseconds)                 

         
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
access_token = '***'

url = f"https://api.extremecloudiq.com/alerts/report"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'startTime': f'{myStartTime}', 'endTime': f'{myEndTime}'}

# serverityIds: None (disabled)
# categoryIds: None (disabled)
# messageMetadataIds: None (disabled)
# acknowledged: None (disabled)
# siteId: None (disabled)
# timeZoneOffset: None (disabled)
# keyword: None (disabled)
# sortField: None (disabled)
# order: None (disabled)
# async: None (disabled)

response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
