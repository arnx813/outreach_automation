import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

def chooseEmails():

    # Use a service account to access the Firestore database
    cred = credentials.Certificate('firestore_key.json')
    firebase_admin.initialize_app(cred)

    # Get a reference to the Firestore database
    db = firestore.client()

    # Read data from a Firestore collection
    collection_ref = db.collection('fortress')
    docs = collection_ref.stream()

    # Convert the data into a list of dictionaries
    data = [doc.to_dict() for doc in docs]

    # Convert the data into a Pandas DataFrame
    df = pd.DataFrame(data)
    df = df[df['emailed'] == False]

    return df.sample(10)


    # change emailed = True
