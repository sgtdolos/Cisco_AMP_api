import requests
from tkinter import *
from tkinter.filedialog import askopenfilename

Tk().withdraw()

#AMP API Credentials
client_id = 'XXXXXXXXXXXXXXXXXXXX'
api_key = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

#AMP Group URL
url = 'https://api.amp.cisco.com/v1/groups/'
#Send API Request
response = requests.get(url, auth=(client_id, api_key))

#print(response.json())
response_json = response.json()

#Get Group name and Group GUID
for group in response_json['data']:
	group_name = group['name']
	group_guid = group['guid']
	print(group_name)
	print(group_guid + "\n")
