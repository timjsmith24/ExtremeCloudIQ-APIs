import requests
         
baseUrl = 'https://api.extremecloudiq.com'
iot_profile_id = 'IoT Profile ID'
access_token = '***'

url = f"{baseUrl}/iot-profiles/{iot_profile_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "app_id": "THREAD_GATEWAY",
  "thread_gateway": {
    "short_pan_id": "BdeC",
    "ext_pan_id": "891d3b931d50869D",
    "master_key": "cE6920E687a2BFdc2AcE6920E687a2BF",
    "network_name": "string",
    "channel": 0,
    "comm_credentials": "g@4D5ipt>vlo MO:B(;1j&\\/Z]O=g4t7~k|@oJyl;Mm0(oF%x~`!,|PDhaSJ3z4gy@xDDS%/F|;L=wFbtQ<O=\"iH2\"daC<T7=@a`yLJ]gOf&@)q\\:R=v2@}0`=J:Nay\\@jxN{6{eiA4U=m-Bp{9)KhzPDp~ zPF2` 1A~Z_e-`-W!#TkD!BohcaM;E3?uL>l=",
    "comm_timeout": 2000000,
    "enable_nat64": True,
    "enable_dns_search_domain": True,
    "white_list": [
      {
        "long_eui": "c5a2fE7dD7E9cf9c",
        "pskd": "X6EFNAD8HAG7YDG62S7LTD0EJ2C9MJYK"
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
        "uuid": "Bc3f38F6-fd76-4086-6C0d-dED65D2FC8F0",
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
        "uuid": "472c209C-d1Ec-CD64-d1aF-5FA3B789bf00",
        "vendors": [
          {
            "vendor_type": "ANY",
            "vendor_name": "string",
            "company_id": 65535
          }
        ],
        "app_type": "IBEACON"
      }
    ]
  }
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
