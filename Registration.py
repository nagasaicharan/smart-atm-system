import pyrebase
from validate_email import validate_email
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522
import cognitive_face as CF
import os
def registration(id,name,email):
    KEY = 'DFHBAKDHBF'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)
    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    
    while(1):
            bol=input("Press 'Y' to take image:\n")
            if bol=='Y':
                # os.system('fswebcam -r 1280x720 1.jpg')
                storage.child("images/"+id+"/original/1.jpg").put("1.jpg")
                url=storage.child("images/"+id+"/original/1.jpg").get_url()
                print(url)
                result = CF.face.detect(url)
                print(result)
                if not result:
                    print("No face Detected in the image")
                else: 
                   print("Please Wait While We Make your Registration....")
                   data= {"id":id,"name": name,"email": email}
                   db = firebase.database()
                   db.child(id).set(data)
                   break



   

    print("Registration Sucessful")
def take_inputs():
    #    reader = SimpleMFRC522()
       id= input("Enter your id: \n")
       name=input("Enter your name: \n")
       while(1):
            email= input("Enter your email: \n")
            is_valid = validate_email(email)
            if is_valid:
                 print("Now place your tag to write")
                 try:
                    reader.write(id)
                    print("Your id is Written to ")
                    registration(str(id),name,email)
                    break
                 finally:
                    GPIO.cleanup()
                    print("Sample")
                
            else:
                print("\nEntered Email ID is not Valid \nPlease Enter your Email id again\n")
config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTHDOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "storageBucket": "YOUR_STORAGE_BUCKET"
  }


firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()
storage =firebase.storage()
take_inputs()
# Get a reference to the database service


# registration("100","Charan","nagasaicharan7@gmail.com")
#db.child("users").set(data)

storage.child("images/100/original/1.jpg").put("1.jpg")
url=storage.child("images/100/original/1.jpg").get_url()
print(url)