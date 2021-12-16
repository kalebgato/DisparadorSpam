import smtplib
import manager_db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def send_mail_spam_all(subject_mail, msg_mail, conf , db_file):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject_mail
    msg['From'] = conf["user"]
    msg.attach(MIMEText(msg_mail, 'html'))
    s = smtplib.SMTP_SSL(conf["host"], conf["port"])
    
    s.login(conf["user"])
    for i in manager_db.cont_rows(db_file) :
        if i!=0:
            db = manager_db.select_value(db_file, i)
            msg['To'] = db[2]
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            print(('Email enviada para %s') % (msg['To']))
    s.quit()
