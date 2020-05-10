# from qrtools.qrtools import QR 
# my_QR = QR(filename = "myqr.png") 
  
# # decodes the QR code and returns True if successful 
# my_QR.decode() 
  
# # prints the data 
# print(my_QR.data)

from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open('myqr.png'))
d=str(d)
i1=d.find("COVID")
i2=d.find("type")
# print(d)
print(d[i1:i2-3])