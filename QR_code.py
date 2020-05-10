from flask import *
from werkzeug.utils import secure_filename
import os
import cv2
from Kerberos import *
import sys

QR = Flask(__name__)

QR.config['UPLOAD_FOLDER'] = 'F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database'

Database = list()

Database.append(HealthCard('Negative',000,'Amit',24,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr'))
Database.append(HealthCard('Negative',111,'Abhishek',22,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr1'))
Database.append(HealthCard('Negative',222,'Shirin',25,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr2'))
Database.append(HealthCard('Negative',333,'Naomi',22,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr3'))
Database.append(HealthCard('Negative',444,'Shraddha',27,'Female','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr4'))
Database.append(HealthCard('Negative',555,'Scott',26,'Male','F:/Semester_08/Network Security/Lab_Assignment_05/Green_QR_code_or_e-pass/Database/myqr5'))


@QR.route('/')
def upload():
    return render_template('HomePage.html')


@QR.route('/uploader', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(QR.config['UPLOAD_FOLDER'],filename))

        res=check(QR.config['UPLOAD_FOLDER']+'/'+filename)
        if res.Status == 'Positive':
            return render_template('Positive.html')

        elif res.Status == 'Negative':
            return render_template('Negative.html')
        else:
            return render_template('Suspected.html')
        #return redirect(url_for('upload',filename=filename))

    return render_template('Homepage.html')

def check(filename):
    data = Database

    uploaded = cv2.imread(filename)


    for i in range(len(data)):
        present = cv2.imread(data[i].Image()+'.png')

        diff = cv2.subtract(uploaded,present)
        b,g,r = cv2.split(diff)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return data[i]




if __name__ == '__main__':
    QR.run(debug=True)
