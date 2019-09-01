# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
import cognitive_face as CF
from sendgrid.helpers.mail import *
# import library 
import math, random 
import pyrebase
#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # by changing value in range 
    for i in range(6) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP

def sendEmail(email):
	print("\n You are not authorized to make this transaction.\n We are Sendind a mail to "+email+" Please find the otp in the email\n Please Wait...")
	sg = sendgrid.SendGridAPIClient('YOUR_SENDGRID_API_KEY')
	from_email = Email("help@smartatmsystem.com")
	to_email = Email(email)
	mail = Mail()
	mail.from_email=from_email
	mail.to_email=to_email
	personalization = Personalization()
	personalization.add_to(to_email)
	otp=generateOTP()
	personalization.dynamic_template_data={
		'OTP':otp
	}
	mail.template_id = "d-07d09332773541c7b1dbbd4ab5d9b04a"
	mail.add_personalization(personalization)
	mail.attachment =Attachment(
        FileContent('base64 encoded content 2'),
        FileName('2.jpg'),
        FileType('image/JPG'))
  

	response = sg.client.mail.send.post(request_body=mail.get())

	print("Check Your Mail box. Email sent Succesfully")
	return otp

def getData(id):
	KEY = 'YOUR_FACE_API_KEY'  # Replace with a valid Subscription Key here
	CF.Key.set(KEY)
	BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
	CF.BaseUrl.set(BASE_URL)
	db = firebase.database()
	storage =firebase.storage()
	data = db.child(str(id)).get()
	k=data.val()
	print("Hi "+k['name']+"!\n Lets take your photo to proceed with transaction\n")
	while(1):
		bol=input("Press 'Y' to take image:\n")
		if bol=='Y':
			os.system('fswebcam -r 1280x720 2.jpg')
			storage.child("images/"+k['id']+"/duplicate/2.jpg").put("2.jpg")
			url_orginal=storage.child("images/"+k['id']+"/original/1.jpg").get_url()
			url=storage.child("images/"+k['id']+"/duplicate/2.jpg").get_url()
			result_orginal = CF.face.detect(url_orginal)
			result=CF.face.detect(url) 
			print(result_orginal)
			if False:
				print("No face Detected in the image")
			else:
				print("Please Wait While We Match your Face..")
				result_verify=CF.face.verify(result_orginal[0]['faceId'],result[0]['faceId'])
				col=False
				if False==col:
					print("You are not authorized to make this transaction.")
					otp=sendEmail(k['email'])
					while(1):
						userotp=input("\n Please Enter Your OTP to Proceed:\n")
						if userotp==otp:
							print("Transaction approved ! Continue with the transaction")
							break
						else:
							print("Entered OTP is wrong! Please Try Again")
				else:
					print("Face matched\n Transaction Successful")
				break
	
	otp=sendEmail(k['email'])
	while(1):
		userotp=input("\n Please Enter Your OTP to Proceed:\n")
		if userotp==otp:
			print("Transaction approved ! Continue with the transaction")
			break
		else:
			print("Entered OTP is wrong! Please Try Again")

	print(data.val())





config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "storageBucket": "YOUR_STORAGE_URL"
  }


firebase = pyrebase.initialize_app(config)
try:
        print("Place your Card to Proceed")	
        id, text = reader.read()
        print("Card Detected! Please remove the card")
        getData(int(900))
        print(text)
finally:
	  print("Success")
        GPIO.cleanup()



