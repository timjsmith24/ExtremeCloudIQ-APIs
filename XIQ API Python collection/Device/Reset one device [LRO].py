import requests

device_id = 769490635896650
access_token = 'eyJraWQiOiIxNzhlZDM3NTVjY2U0YWEzODg5MTY5N2YyNjFlMGUzZCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ0aXNtaXRoK2FwaUBleHRyZW1lbmV0d29ya3MuY29tIiwic2NvcGVzIjpbImxvZ291dCIsImF1dGgiLCJhdXRoOnIiLCJ0b2tlbjpuZXciLCJwZXJtOmNoZWNrIiwibHJvIiwibHJvOnIiLCJhY2NvdW50IiwiYWNjb3VudDpyIiwidmlxOmJhY2t1cCIsInVzZXIiLCJ1c2VyOnIiLCJoaXEiLCJoaXE6ciIsIm9yZyIsIm9yZzpuZXciLCJvcmc6ZGVsIiwib3JnOnJlbmFtZSIsImhpcS5jdHgiLCJoaXEuY3R4OnIiLCJoaXEuY3R4OnciLCJkZXZpY2UiLCJkZXZpY2U6ciIsImRldmljZTpsaXN0IiwiZGV2aWNlOnZpZXciLCJkZXZpY2U6bmV3IiwiZGV2aWNlOmRlbCIsImRldmljZTpjbGkiLCJkZXZpY2U6ZGVwbG95IiwiZGV2aWNlOm1hbmFnZSIsImRldmljZTp1bm1hbmFnZSIsImRldmljZTpyZWJvb3QiLCJkZXZpY2U6cmVzZXQiLCJjbGllbnQiLCJjbGllbnQ6ciIsImxvY2F0aW9ucyIsImxvY2F0aW9uczpyIiwibmV0d29yay1wb2xpY3kiLCJwb2xpY3k6c3NpZCIsIm5ldHdvcmstcG9saWN5OnIiLCJzc2lkIiwic3NpZDpyIiwicGNnOmtleSIsInBjZzprZXk6ciIsInN1YnNjcmlwdGlvbnMtd2ViaG9vayIsInN1YnNjcmlwdGlvbnMtd2ViaG9vazpyIiwiY2NnIiwiY2NnOnIiLCJsb2ciLCJsb2c6ciIsImN3cCIsImN3cDpyIiwic21zLXRtcGwiLCJzbXMtdG1wbDpyIiwiY2xhc3MtcnVsZSIsImNsYXNzLXJ1bGU6ciIsInVzZXItcHJvZmlsZSIsInVzZXItcHJvZmlsZTpyIiwicmFkaXVzLXByb3h5IiwicmFkaXVzLXByb3h5OnIiLCJyYWRpdXMtc2VydmVyIiwicmFkaXVzLXNlcnZlcjpyIiwidXNlcmdyb3VwIiwidXNlcmdyb3VwOnIiLCJkZXBsb3ltZW50IiwiZGVwbG95bWVudDpyIiwiYWQtc2VydmVyIiwiYWQtc2VydmVyOnIiLCJhbGVydCIsImFsZXJ0OnIiLCJhcHAiLCJhcHBsaWNhdGlvbjpyIiwibDMtYWRkcmVzcy1wcm9maWxlIiwibDMtYWRkcmVzcy1wcm9maWxlOnIiLCJ2bGFuLXByb2ZpbGUiLCJ2bGFuLXByb2ZpbGU6ciIsImVuZHVzZXIiLCJlbmR1c2VyOnIiLCJyYWRpdXMtY2xpZW50LW9iamVjdCIsInJhZGl1cy1jbGllbnQtb2JqZWN0OnIiLCJsZGFwLXNlcnZlciIsImxkYXAtc2VydmVyOnIiLCJlbWFpbC10ZW1wbGF0ZSIsImVtYWlsLXRlbXBsYXRlOnIiLCJjZXJ0aWZpY2F0ZSIsImNlcnRpZmljYXRlOnIiXSwidXNlcl9pZCI6MjE3OTIzMjEsInJvbGUiOiJBZG1pbmlzdHJhdG9yIiwiY3VzdG9tZXJfaWQiOjIxNzkxOTcxLCJjdXN0b21lcl9tb2RlIjowLCJoaXFfZW5hYmxlZCI6ZmFsc2UsIm93bmVyX2lkIjoxNzkxNjEsIm9yZ19pZCI6MCwiZGF0YV9jZW50ZXIiOiJJQV9HQ1AiLCJzaGFyZCI6IlVTIiwianRpIjoiNTQzNWE0MzZkMGUzNGFlMDg4MmMyODY0NzA5YTBlMjAiLCJpc3MiOiJodHRwczovL3VzMC5leHRyZW1lY2xvdWRpcS5jb20iLCJpYXQiOjE2NzY2NDMyMzAsImV4cCI6NDgzMDI0MzIzMH0.COy3IpHNE3tFrLn9Hx1x3Ti8rchSo6CtRAjfc-i1fRT8eALPFKmBrbrJIGLetu2fPQ0WiFCHkfWSYRTENGzOxhd-mkyMglNfklPlyec3Sw4Kc2v0d9Btm78YLs9T9y4L7_1HMimvGBc9vrxtX0ZXP2vSOkvoA_6kWrunhBIGNLv5eQ2dwdVvSK9DsVET6JWAdcXfED8vS_WboSqaOGiWyKtHyG9K5Z1glViksH0kVwMLwm_nACEYcmJMqhZWY6-xrC47s_JgU_un24q0CK0WOignM0Dgve6-pyuPjV7G54v_0tgPEAblBbbXZutl8ygFWtLKNw9F2SYjl7qfDFd3_w'

url = f"https://api.extremecloudiq.com/devices/{device_id}/:reset?async=true"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)

print(f"Long Running Status URL - {response.headers['Location']}")
