import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('medical-results-firebase-adminsdk-v5181-6ea14e057b.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

Obj1 = {
    "Name": "Mike Smith",
    "Age": 20,
    "Sodium": 140
}

Obj2 = {
    "Name": "Sarah Cooper",
    "Age": 48,
    "Sodium": 138
}

data = [Obj1, Obj2]

for record in data:
    doc_ref = db.collection('Patients').document(record['Name'])
    doc_ref.set(record)