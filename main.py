import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
URI = "mongodb+srv://opencartplugin:Makian1!@mycluster.3eoowbm.mongodb.net/?retryWrites=true&w=majority&appName=mycluster"
DBNAME = "parkdb"

client = MongoClient(URI, server_api=ServerApi('1'))
db = client[DBNAME]

print("Loading User Data ...", flush=True, end="")
docs = db.userAccess.find()
ALLOWED_IDS = [doc['userid'] for doc in docs]


st.write(ALLOWED_IDS)
# st.write("hello wai")

