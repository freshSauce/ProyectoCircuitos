import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase:
    def __init__(self):
        self.cred = credentials.Certificate('app/key.json')
        self.data = None
        self.ref = None
        

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': "https://asistencia-itspa-default-rtdb.firebaseio.com/"
        })

        if not self.ref:
            self.ref = db.reference('pase_de_lista')
        
    
    def fetch(self, reference):
        self.ref = db.reference(reference)
        data = self.ref.order_by_key().get()
        self.data = data
        return self.data
    
    def pagination(self, step=5):
        self.data = self.fetch('pase_de_lista')
        data_length = len(self.data)
        pages = data_length // step
        if data_length % step != 0:
            pages += 1
        for page in range(pages):
            start = page * step
            end = start + step
            yield self.ref.order_by_key().start_at(str(start)).end_at(str(end - 1)).get()
