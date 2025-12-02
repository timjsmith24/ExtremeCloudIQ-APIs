import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/iot-profiles"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "app_id": "THREAD_GATEWAY",
  "thread_gateway": {
    "short_pan_id": "7ecD",
    "ext_pan_id": "fEf978cd84e60ffF",
    "master_key": "B9704A19e8ab939F9EaC55DFbCfd07Cb",
    "network_name": "string",
    "channel": 0,
    "comm_credentials": "kwiOq1VqD+DtEquZ_yk>pjC<nOz^`H  \\inj1vTZeY fN@?e~'AI;KG0@ LA<j4VWCWVg*ce:>)!]]&gl!dHxTB(6A 9xPI@)%8\"_>B9zR>ae3",
    "comm_timeout": 2000000,
    "enable_nat64": True,
    "enable_dns_search_domain": True,
    "white_list": [
      {
        "long_eui": "*",
        "pskd": "JL53DD9"
      }
    ],
    "default_user_profile_id": 0
  },
  "app_supported": "SINGLE",
  "ble_beacon": {
    "applications": [
      {
        "measured_rss": 15,
        "advertise_interval": 10240,
        "tx_power": 3,
        "major": 65535,
        "minor": 65535,
        "uuid": "Fc5bb1BE-6318-496F-b08d-5BF8682DD353",
        "url": "string",
        "app_type": "IBEACON"
      }
    ]
  },
  "ble_scan": {
    "destination": {
      "interval": 60,
      "http_server": {
        "url": "string",
        "interval": 60,
        "enable_deduplication": True
      }
    },
    "applications": [
      {
        "min_rss": 20,
        "uuid": "Aa817E2f-6b42-bcC1-8FF4-c542134b012B",
        "vendors": [
          {
            "vendor_type": "ANY",
   


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
