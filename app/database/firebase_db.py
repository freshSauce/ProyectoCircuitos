import tempfile
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import pandas as pd
import json

class Firebase:
    def __init__(self):
        if os.environ.get("FLASK_ENV") == "production":
            self.cred = credentials.Certificate('/etc/secrets/key.json')
        else:
            self.cred = credentials.Certificate('app/key.json')
        self.data = None
        self.ref = None
        

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': "https://asistencia-itspa-default-rtdb.firebaseio.com/"
        })

        if not self.ref:
            self.ref = db.reference('ruta_en_la_database')
        
    
    def fetch(self, reference):
        self.ref = db.reference(reference)
        data = self.ref.order_by_key().get()
        self.data = data
        return self.data
    
    def pagination(self, step=5):
        self.data = self.fetch('ruta_en_la_database')
        local_data = [self.data[key] for key in self.data.keys()]
        self.data = local_data
        data_length = len(self.data)
        pages = data_length // step
        if data_length % step != 0:
            pages += 1
        for page in range(pages):
            start = page * step
            end = start + step
            yield self.data[start:end]
    
    def export_to_excel(self):
        self.data = self.fetch('ruta_en_la_database')
        df = pd.read_json(json.dumps(self.data))
        with tempfile.NamedTemporaryFile(mode='r+') as temp:
            df.to_excel(temp.name + ".xlsx")
        return temp.name + ".xlsx"