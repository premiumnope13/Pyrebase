import pyrebase
import os
import time

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "test-nodemcu-5ea41",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("", "")

db = firebase.database()
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']
                        #INPUT SOME DATA 
#nameInput = input("Write The name : ")
#agentInput = input("Write The Agent :  ")

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
    temp = os.popen("vcgencmd measure_temp").readline()
    print()
    archer = measure_temp()
    print(temp)
    time.sleep(2.5)
    db.child("temp").set(archer,user['idToken'])
#all_agents = db.child("orders").get(user['idToken']).val()


#                       #RETRIEVE VIA ID

# all_agents = db.child("agents").get(user['idToken']).val()
# print (all_agents)

#                    #CHANGING AGENCY DATA

# agency_replace = input("Data to replace: ")
# agency_replace_to = input ("New Data: ")
#                       #UPDATE SOME DATA 

# for i in all_agents:
#    if all_agents[i]['agency'] == agency_replace:
#     all_agents[i]['agency'] = agency_replace_to
#     print (all_agents[i]['agency'])
#     print (all_agents)
#     db.child("agents").set(all_agents,user['idToken'])





#Add by custom Key
#aggregate_input = {"fullname": "Lana Kane", "notes": "Figgis Agency"}
