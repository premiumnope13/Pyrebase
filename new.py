import pyrebase

config = {
  "apiKey": "AIzaSyBsrnOhng4Zp3dYcraVtx_eM8vKN9lIhDs",
  "authDomain": "test-nodemcu-5ea41.firebaseapp.com",
  "databaseURL": "https://test-nodemcu-5ea41.firebaseio.com",
  "storageBucket": "test-nodemcu-5ea41"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("budi.aulian.h@gmail.com", "Gjwzjbsajkrf1234")

db = firebase.database()
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']

aulian = "busi"

#add by unique key
#archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
#db.child("agents").push(archer, user['idToken'])

#Add by custom Key
# lana = {"fullname": "Lana Kane", "notes": "Figgis Agency"}

# db.child("orders").child(aulian).set(lana, user['idToken'])

all_agents = db.child("orders").get(user['idToken']).val()

cars = ["BWW","FIAT","HONDA"]
print (cars)
#READ TROUGH ARRAY
for i in range(len(cars)):
  print (cars[i])
#READ TROUGH DIRECTORY
for  i in all_agents:
     
     n = ( all_agents[i]['fullname']) 
     print (n)

