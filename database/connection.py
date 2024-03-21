import firebase_admin
from firebase_admin import credentials, firestore
from secret.vars_ambiente import MY_SECRETS

cred = credentials.Certificate(MY_SECRETS)
firebase_admin.initialize_app(cred)
db = firestore.client()

print(cred)

def get_docs_ambos():
    return db.collection('cartaoAmbos').get()


def get_docs_cartaorapha():
    return db.collection('cartaoRapha').get()


def get_docs_cartaorhai():
    return db.collection('cartaoRhai').get()


database_ambos = []
database_rapha = []
database_rhai = []

docs_cartaoRapha = get_docs_cartaorapha()
docs_cartaoRhai = get_docs_cartaorhai()
docs_ambos = get_docs_ambos()

for doc_rapha in docs_cartaoRapha:
    doc_data_rapha = doc_rapha.to_dict()
    doc_data_rapha['id'] = doc_rapha.id
    database_rapha.append(doc_data_rapha)

for doc_rapha in docs_cartaoRapha:
    doc_data_rapha = doc_rapha.to_dict()
    doc_data_rapha['id'] = doc_rapha.id
    database_rapha.append(doc_data_rapha)


for doc_ambos in docs_ambos:
    doc_data_ambos = doc_ambos.to_dict()
    doc_data_ambos['id'] = doc_ambos.id
    database_ambos.append(doc_data_ambos)

