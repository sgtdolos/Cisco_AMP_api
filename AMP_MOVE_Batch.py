import requests
from tkinter import *
from tkinter.filedialog import askopenfilename

#Get rid of Tk box
Tk().withdraw()

#AMP API Credentials
client_id = 'XXXXXXXXXXXXXXXXXXXX'
api_key = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

#Request Group GUID from User
group_guid = input("Group GUID: ")

#Request Computer GUID list file from User, open and split lines
print("Select file with list of Computer GUIDs: ")
guid_list = askopenfilename()
with open(guid_list, "r") as f:
	list_guids = f.read().splitlines()
f.close()

#API call to move each Computer GUID to the Group GUID
for computer_guid in list_guids:
	url = 'https://api.amp.cisco.com/v1/computers/{}'.format(computer_guid)
	response = requests.patch(url, auth=(client_id, api_key), data={'group_guid':group_guid})
#	print(response.json())
	response_json = response.json()
	hostname = response_json["data"]["hostname"]
	group_link = response_json["data"]["links"]["group"]
	print(hostname + " has been moved to group at " + group_link)
	
