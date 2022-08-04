from fastapi import FastAPI
import requests
import uvicorn, hashlib
from pymongo import MongoClient

app = FastAPI()

myClient = MongoClient()
mydb = myClient["myDB"]
myCol = mydb["customers"]

def hashPassword(password):
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed

@app.get("/")
def check(email, password, subject, body,reciever):
    if(myCol.find_one({"email": email})):
        if(myCol.find_one({"email": email})['password'] == hashPassword(password)):
            param = {"email" : email,
                     "password" : password,
                     "subject" : subject,
                     "body" : body,
                     "reciever" : reciever}
            requests.get('http://127.0.0.1:8000/send', params= param)
            return "Wait"
        else:
            return "Wrong password"
    else:
        mydict = {"email":email, "password": hashPassword(password)}
        myCol.insert_one(mydict)
        return "register new email"

if __name__ == "__main__":
    uvicorn.run('check:app', reload=True, port=5000)