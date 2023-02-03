import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from add_email_funcs.create_identifier import create_identifier

def add_email(csv):

    ########################################################
    #        IMPORT CSV OF NEW CONTACTS INTO DATAFRAME
    ########################################################
    import pandas as pd
    df = pd.read_csv("./test/df.csv")

    ########################################################
    #     HASH FUNCTION TO CREATE ID (PREVENTS DUPLICATES)
    ########################################################
    for index, row in df.iterrows():
        df.at[index, 'id'] = create_identifier(row['firstName'], row['lastName'], row['email'])

    print(df['id'])

    ########################################################
    #        ADD CONTACTS TO FIRESTORE
    ########################################################
    cred = credentials.Certificate('firestore_key.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    # iterate through dataframe. if identifier is not already in the database, add to database.
    for index, row in df.iterrows():
        doc_ref = db.collection(u'fortress').document(row['id'])
        doc_ref.set({
            u'email': row['email'],
            u'emailed': False,
            u'firstName': row['firstName'],
            u'lastName': row['lastName'],
            u'title': row['job']
        })