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

for x in root.findall('entry'):
  item = x.find('x'.attrib)
  print(item)
print(root.tag)       #response
print(root[0][0])     #<Element 'config' at 0x7f8e3b3cae00>
print(root[0][0][0])    #<Element 'panorama' at 0x7f833e96ec70>
print(root[0][0][0][0][0][0].tag)



def print_one_by_one(text):
  sys.stdout.write("\r " + " " * 60 + "\r")
  sys.stdout.flush()
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.01)

def invalid_choice():
  print()
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print_one_by_one("      ~ Invalid Choice. Please try again. Thank you! ~\n")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print()
  print()



while True:
  rule_choice = input("""\nPlease choose which rule you want to check: \n
        1:  intrazone-default
        2:  interzone-default\n

    Your choice: """)

  if rule_choice == '1':
    rule_choice = 'intrazone-default'
    break
  elif rule_choice == '2':
    rule_choice = 'interzone-default'
    break
  else:
    invalid_choice()








for default_rule in root.iter('default-security-rules'):    # vsys1 and vsys2
  check = default_rule.find('rules')
  #print(check[1].attrib)     #{'name': 'intrazone-default', 'uuid': '65b88377-cca2-4a9c-9b10-3251891b2c09'};
                              # {'name': 'interzone-default', 'uuid': '3dd418c5-2517-40e4-a84c-dc21b71ecb01'}
  name = check[1].attrib.get('name')
  # print(name)                 #intrazone-default;  interzone-default
  # print(check.tag)            # rules; rules;
  # print(check[0].tag)         # entry
  # print(check[0][0].tag)      # action
  # print(check[0][0].text)     # allow
  # print(check[1][0].text)     # deny
  action_intrazone = check[1][0].text
  action_interzone = check[0][0].text


  if rule_choice == "intrazone-default":
    print_one_by_one('*' * 80)
    print()
    print_one_by_one(f'      Rule "{rule_choice}" exists, the action of this rule is: {action_intrazone}\n')
    print_one_by_one('*' * 80)
    print()
    break
  elif rule_choice == "interzone-default":
    print_one_by_one('*' * 80)
    print()
    print_one_by_one(f'      Rule "{rule_choice}" exists, the action of this rule is: {action_interzone}\n')
    print_one_by_one('*' * 80)
    print()
    break
  else:
    print(f'The rule {rule_choice} does not exist')


  # if 'rule_choice' in name:
  #    print(f'The rule "{'rule_choice'}" exists, the action is {action}')








  # print(name)
  #print(check[1][0].tag)

# for rule_check in root.iter('intrazone-default'):
#   print(rule_check.tag)


# root2 = root.iter('default-security-rules')
# print(root2[0][0])

# print(root.tag)                                                     # response
# print(root.attrib)                                                 # {'status': 'success'}
# print(root.findall('name="intrazone-default"'))       # []
# print(root[0][0])                                     # <Element 'config' at 0x7f7f0ff43ef0>
#
# print(root[0][0][0][0])                               #<Element 'certificate' at 0x7f0aedc4f540>
#
# print(root.find('<entry name="interzone-default" uuid="3dd418c5-2517-40e4-a84c-dc21b71ecb01">'))


# for rule_name in root.findall('name="intrazone-default"'):
#   print(rule_name.attrib)
#   print(rule_name.text)
# tree = ET.fromstring(response.text)
# root = tree.getroot()
# if rule_name in root.findall('name="intrazone-default"'):
#   print(True)


# print(tree.find('default-security-rules'))
# print(tree.find('interzone-default'))
# tree.find('default-security-rules')
# tree.find('interzone-default')

# root = tree.getroot()
# rule_name = root.get('interzone-default')
#
#
# for child in root.iter('default-security-rules'):
#   print(child.attrib)



# for child in root:
#   if child == 'default-security-rules':
#     print(child)
#


# root = ET.fromstring(response.text)
# for child in root.findall('default-security-rules'):
# # for child in root:
#     print(child.tag, child.attrib)
# #
# # print(root.findall('default-security-rules'))
# #print(response.text)


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