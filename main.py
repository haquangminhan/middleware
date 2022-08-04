from fastapi import FastAPI
import uvicorn, hashlib
from pymongo import MongoClient

from sendMail import send
app = FastAPI()

myClient = MongoClient()
mydb = myClient["myDB"]
myCol = mydb["customers"]

# def hashPassword(password):
#     hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
#     return hashed

# def check(email, password):
#     if(myCol.find_one({"email": email})):
#         if(myCol.find_one({"email": email})['password'] == hashPassword(password)):
#             return "Successful"
#         else:
#             return "Wrong password"
#     else:
#         return "register new email"

@app.get("/send")
def saveData(email, password, subject, body,reciever):
    # if (check(email, password) == "register new email"):
    #     mydict = {"email":email, "password": hashPassword(password)}
    #     myCol.insert_one(mydict)
    #     return "register successfully!!!"
    # elif(check(email, password) == "Successful"):
    print(email, password, subject, body,reciever)
    send(email, password, subject, body,reciever)
    print ("Successful")
    #     return "Sent successfully!!!!"
    # else:
    #     return "Wrong password"


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)