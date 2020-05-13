from flask import *
from werkzeug.utils import secure_filename
import os
import cv2
from Testing_Labs import *

import pandas

from Crypto.Cipher import AES
from Crypto import Random

Result = None
Aes_key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

QR = Flask(__name__)

QR.config['UPLOAD_FOLDER'] = 'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database'

File = ""


# ---------- Uploading the QR Code --------------------
@QR.route('/upload', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(QR.config['UPLOAD_FOLDER'],filename))

        file_name = QR.config['UPLOAD_FOLDER']+'/'+filename

        global File
        File = File+file_name
        input_file = open(file_name,'rb')
        input_data = input_file.read()
        input_file.close()

        # ------- Creating the hash of the Image ------------
        Img_hash = hashlib.md5(input_data).digest()

        # ---------- Encrypting the Image -----------------
        cipher = AES.new(Aes_key,AES.MODE_CFB,iv)
        enc_data = cipher.encrypt(input_data)
        res = check(enc_data,Img_hash)

        if res['Status'] == 'Positive':
            res.Id = str(res[0])
            res.Age = str(res[3])
            return render_template('Positive.html', result=res)

        elif res['Status'] == 'Negative':
            res.Id = str(res[0])
            res.Age = str(res[3])
            return render_template('Negative.html', result=res)
        elif res['Status'] == 'Suspected':
            res.Id = str(res[0])
            res.Age = str(res[3])
            return render_template('Suspected.html', result=res)
        else:
            return "Wrong QR Code"
        #return redirect(url_for('upload',filename=filename))

    return render_template('HomePage.html')

# -------------- Authentication Function ------------------
def check(data,hash):

    Aes_decipher = AES.new(Aes_key,AES.MODE_CFB,iv)
    plain_data = bytearray(Aes_decipher.decrypt(data))

    if str(hashlib.md5(plain_data).digest()) == str(hash):
        data1 = pandas.read_csv('Details.csv')


        for i in range(len(data1)):
            present = cv2.imread(data1['Path'][i]+'.png')
            plain = cv2.imread(File)
            b,r,g = cv2.split(cv2.subtract(present,plain))
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                return data1.loc[i]




if __name__ == '__main__':
    QR.run(debug=True)
