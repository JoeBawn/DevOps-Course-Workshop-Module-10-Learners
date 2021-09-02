import requests

url = "https://login.microsoftonline.com/41ce3039-1fb8-4502-afaa-4adbb8ec9a69/oauth2/v2.0/token"

payload='client_id=a8159431-9917-4058-96a9-859f9a8c1fb5&scope=71f15ba7-7d5a-4849-97aa-9acd41ab5396%2F.default&client_secret=sR6R9-_.T.S1E.1X92VpW1I08F2SwkZz-z&grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'x-ms-gateway-slice=estsfd; stsservicecookie=estsfd; fpc=Air3VV3vZMZAqhMeNdW_MB-nBIdBAQAAAConwNgOAAAA'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
