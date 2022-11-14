import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
login = credentials.Certificate("key.json")

def submit(name,email_id,phone_number,message):
   db=firestore.client()
  feedback=db.collection("Feedback")
  feedback.document().set({
    'Name': name,
    'Phone Number': phone_number,
    'Email Id':email_id,
    'Feedback': message
    })
