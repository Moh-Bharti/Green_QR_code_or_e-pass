from flask import *
#from werkzeug.utils import secure_filename
import os
import hashlib
import sys
from flask_login import LoginManager
from flask_login import login_required
from cryptography.fernet import Fernet
from des import DesKey


key_suite = Fernet(Fernet.generate_key())

class HealthCard:

    def __init__(self, Status, Id,Name, Age, Gender, Path ):
        self.Status = Status
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Path = Path

    def Image(self):
        return self.Path

    def Bio(self):
        return self.Status, self.Id, self.Name, self.Age, self.Gender



Labs = {'Cipla':'1935','SunPharma':'1983','Lupin':'1968','Cadila':'1952','Glenmark':'1977'}

Lab = Flask(__name__)

Lab.secret_key = b'Moh_Abhishek_247_006'


#login_manager = LoginManager()
#login_manager.init_app(Lab)
S1 = "Hello"
Cipher = key_suite.encrypt(S1.encode())

@Lab.route('/Lab', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        Pass = hashlib.md5(str(request.form['password']).encode())
        word = Pass.digest()


        key = DesKey(word)

        req = key.encrypt(user.encode(), padding=True)

        redirect(url_for('ticket',token=req))
        #print(tick, 'hi',file=sys.stdout)
        global Cipher
        print(key_suite.decrypt(Cipher),file=sys.stdout)
        return redirect(url_for('suc',card=Cipher))




    return render_template('Lab_login.html',error=error)

@Lab.route('/authenticate/<token>')
def ticket(token):

    user_info = Labs.keys()
    pass_info = Labs.values()

    S = ""
    for i in range(len(user_info)):
        locution  = hashlib.md5(pass_info[i].encode())
        cue = locution.digest()
        key = DesKey(cue)
        user = key.decrypt(token,padding=True)

        if user == user_info[i].encode():

            S = S+"Give the access"

    global Cipher
    if S == "Give the access":
        ciphertext = key_suite.encrypt(S.encode())

        Cipher = ciphertext

    else:
        S = "Don't give the access"
        ciphertext = key_suite.encrypt(S.encode())

        Cipher = ciphertext


@Lab.route('/success/<card>', methods=['GET', 'POST'])

def suc(card):
    dec_card = key_suite.decrypt(card)
    if dec_card == "Give the access":
        if request.method == 'POST':
            Id = request.form['Id']
            status = request.form['status']
            a = -1
            for i in range(len(Database)):

                if Database[i].Id == int(Id):
                    a += i+1

            if a >= 0:

                Database[a].Status = status
                return "Updated Successfully"
    else:
        return "Wrong Id"

    return render_template('Update.html', error=None)



if __name__=='__main__':
    Database = list()

    Database.append(HealthCard('Negative', 000, 'Amit', 24, 'Male',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr'))
    Database.append(HealthCard('Negative', 111, 'Abhishek', 22, 'Male',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr1'))
    Database.append(HealthCard('Negative', 222, 'Shirin', 25, 'Female',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr2'))
    Database.append(HealthCard('Negative', 333, 'Naomi', 22, 'Female',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr3'))
    Database.append(HealthCard('Negative', 444, 'Shraddha', 27, 'Female',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr4'))
    Database.append(HealthCard('Negative', 555, 'Scott', 26, 'Male',
                               'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr5'))

    Lab.run(debug=True)





