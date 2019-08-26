import pyrebase

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth() 
#authenticate a user
user = auth.sign_in_with_email_and_password("Joejoster.", "")

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

<<<<<<< HEAD
=======
colors = ["red","green","blue"]

for i in range(len(colors)):
  print (colors[i])
>>>>>>> 63a628bdcf17910f232d9e69979f44fb9994634e
