import pyrebase

config = {
  "apiKey": "AIzaSyBsrnOhng4Zp3dYcraVtx_eM8vKN9lIhDs",
  "authDomain": "test-nodemcu-5ea41.firebaseapp.com",
  "databaseURL": "https://test-nodemcu-5ea41.firebaseio.com",
  "projectId": "test-nodemcu-5ea41",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("budi.aulian.h@gmail.com", "Gjwzjbsajkrf1234")

db = firebase.database()
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']



#INPUT SOME DATA 
# def agentInput(archer,):

#   archer['name'] = input("Agent Name: ")
#   archer['agency'] = input ("Agency : ")
  
  
#   return

# agent_name_input =  "String"
# agent_agency_input = "String"
# archer = {"name": agent_name_input, "agency": agent_agency_input}

# agentInput(archer)
# db.child("agents").push(archer, user['idToken'])

# all_agents = db.child("orders").get(user['idToken']).val()


                      #RETRIEVE VIA ID
all_agents = db.child("agents").get(user['idToken']).val()
print (all_agents)

                   #CHANGING AGENCY DATA
agency_replace = input("Data to replace: ")
agency_replace_to = input ("New Data: ")
                      #UPDATE SOME DATA 

for i in all_agents:
   if all_agents[i]['agency'] == agency_replace:
    all_agents[i]['agency'] = agency_replace_to
    print (all_agents[i]['agency'])
    print (all_agents)
    db.child("agents").set(all_agents,user['idToken'])



#add by unique key
#archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
#db.child("agents").push(archer, user['idToken'])

#Add by custom Key
#aggregate_input = {"fullname": "Lana Kane", "notes": "Figgis Agency"}




