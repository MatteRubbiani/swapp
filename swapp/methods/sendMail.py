from itsdangerous import URLSafeTimedSerializer
import smtplib
import hashlib, uuid


def sendmail (mail, username):
    s = URLSafeTimedSerializer("password1")
    token=s.dumps(mail, salt="emailconfirm")
    #link="http://127.0.0.1:5000/confirm/"+token
    link="https://smartmates.herokuapp.com/confirm/"+token
    subject="Confirm your account on Swapp"

    text ="""

Hi {}!
Thanks for signing up!
Click the link below to confirm your email adress and start using your account!


{}

If you didn't ask for an account don't worry, someone probably misspelt their email address.


Kind Regards,

Team SmartMates


     """.format(username,link)
    message = 'Subject: {}\n\n{}'.format(subject, text)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("smartmates2018@gmail.com", "smartmates1")
    server.sendmail("smartmates2018gmail.com", mail, message)
