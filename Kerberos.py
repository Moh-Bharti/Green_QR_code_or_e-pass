from flask import *
#from werkzeug.utils import secure_filename
import os
import hashlib
import sys
from flask_login import LoginManager
from flask_login import login_required

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


Database = list()

Database.append(HealthCard('Negative',000,'Amit',24,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr'))
Database.append(HealthCard('Negative',111,'Abhishek',22,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr1'))
Database.append(HealthCard('Negative',222,'Shirin',25,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr2'))
Database.append(HealthCard('Negative',333,'Naomi',22,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr3'))
Database.append(HealthCard('Negative',444,'Shraddha',27,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr4'))
Database.append(HealthCard('Negative',555,'Scott',26,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr5'))

Labs = {'Cipla':'1935','SunPharma':'1983','Lupin':'1968','Cadila':'1952','Glenmark':'1977'}

Lab = Flask(__name__)

Lab.secret_key = b'Moh_Abhishek_247_006'

#login_manager = LoginManager()
#login_manager.init_app(Lab)


@Lab.route('/Lab', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        word = request.form['password']

        User_info = Labs.keys()
        Pass_info = Labs.values()

        if User_info.__contains__(user) and Labs.get(user) == word:
            return redirect(url_for('suc'))


        else:
            return "Wrong Login or Password, Please Try Again"

    return render_template('Lab_login.html',error=error)


@Lab.route('/success', methods=['GET', 'POST'])
#@login_required
def suc():

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
    Database
    Lab.run(debug=True)





