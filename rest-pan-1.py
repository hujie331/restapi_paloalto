import pprint
import json
import _json
import requests
import xmltodict

from urllib3.exceptions import InsecureRequestWarning   # to clear the self-assigned authentication alarm
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # to clear the self-assigned authentication alarm

url = "https://172.19.195.44/api/?REST_API_TOKEN=28395583&type=op&cmd=%3Cshow%3E%3Cconfig%3E%3Crunning%3E%3C%2Frunning%3E%3C%2Fconfig%3E%3C%2Fshow%3E"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/xml',
  'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
  'Cookie': 'PHPSESSID=1013d8d275427d33c87d7f7389209066'
}

response = requests.request("GET", url, verify=False, headers=headers, data=payload)  # 'verify=False,' is mandatory, otherwise the code will be interrupted when runnin.

if "interzone-default" in response.text:
  print(True)
print(response.text)
# response_dict = json.loads(response)
# print(type(response_dict))
#print(type(response.text))
# response_dict = xmltodict.parse(response.text)
# print(type(response_dict))
# pprint.pprint(response_dict)(77)
# ttt = json.dumps(response.text)
# tttt = response.json()
# print(type(response))
# print(type(response.text))
# print(type(ttt))
# print(type(tttt))
# #print(type(response.json()))
#print(type(response.json.loads()))
#print(response.json)
#response_dict = response.json()
#print(type(response.content))
#print(response.content)
#pprint.pprint(response.text)

#pprint.pprint(response_dict)