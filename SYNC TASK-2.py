import os
import math
import random
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("tharunkumarvanama@gmail.com", "wpbr tqer ufii yill")
emailid=input("Please Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP : ")
if a == OTP:
    print("OTP Verified")
else:
    print("Wrong OTP!..Please enter correct OTP")