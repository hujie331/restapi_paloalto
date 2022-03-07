from pprint import pprint
import json
import _json
import requests
import xmltodict
import sys,time
import xml.etree.ElementTree as ET

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

response = requests.request("GET", url, verify=False, headers=headers, data=payload)  # 'verify=False,' is mandatory, otherwise the code will be interrupted when running.

#print(type(response)) #<class 'requests.models.Response'>

# if "interzone-default" in response.text:
#   print(True)

# how to parse xml:   https://www.youtube.com/watch?v=r6dyk68gymk
root = ET.fromstring(response.text)
#print(root)                 #<Element 'response' at 0x7fe194da76d0>
print(root[0][0])           #config
print(root[0][0][0])        #panorama 27837
print(root[0][0][0][0])     #certificate  27838
print(root[0][0][0][0][0])  #entry 27839
print(root[0][0][0][0][2])  #entry  27975
print(root[0][0][0][0][2][0]) #subject-hash


#root.getchildren().index('default-security-rules')
#root.getchildren().index(response)
# root.list(response)
# root.index





#
# for default_rule in root.iter('default-security-rules'):
#   check = default_rule.find('rules')
#   #print(check[1].attrib)     #{'name': 'intrazone-default', 'uuid': '65b88377-cca2-4a9c-9b10-3251891b2c09'};
#                               # {'name': 'interzone-default', 'uuid': '3dd418c5-2517-40e4-a84c-dc21b71ecb01'}
#   name = check[1].attrib.get('name')
#   # print(name)                 #intrazone-default;  interzone-default
#   # print(check.tag)            # rules; rules;
#   # print(check[0].tag)         # entry
#   # print(check[0][0].tag)      # action
#   # print(check[0][0].text)     # allow
#   # print(check[1][0].text)     # deny
#   action_interzone = check[1][0].text
#   action_intrazone = check[1][0].text
#
