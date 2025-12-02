import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/:onboard"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "extreme": {
    "sns": [
      "string"
    ]
  },
  "exos": {
    "sns": [
      "string"
    ]
  },
  "voss": {
    "sns": [
      "string"
    ]
  },
  "wing": {
    "sn_to_mac": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  },
  "dell": {
    "sn_to_st": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  },
  "dt": {
    "dts": [
      {
        "make": "SWITCH_ENGINE",
        "model": "DT_5320_16P_4XE",
        "os_type": "string",
        "os_version": "string",
        "vim_modules": [
          "DT_5520_VIM_4X"
        ],
        "feat_licenses": [
          "PRD_5000_PRMR"
        ]
      }
    ]
  }
}


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
