# User_info = dict({'moh':[123,2016111],'abhishek':[234,2016006],'lakshay':[456,2016222],'kanha':[908,2016333]})
# print(User_info.keys())
# print(User_info.values())
# import hashlib
# p = hashlib.sha3_512("2016006".encode()).hexdigest()
# print(type(p))
# password=input("Enter the password : ")
# print(p)
# print(hashlib.sha3_512(password.encode()).hexdigest()==p)
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = "ID: 555,COVID STATUS : NEGATIVE"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 

  
# Create and save the png file naming "myqr.png" 
url.png('qr.png', scale = 6)