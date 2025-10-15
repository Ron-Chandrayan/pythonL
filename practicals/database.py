import smtplib
from email.message import EmailMessage

#creating the mail
msg=EmailMessage()
msg['From']='chandrayanpaul27@gmail.com'
msg['To']='chandrayanpaul27@gmail.com'
msg['Subject']='Testing'
msg.set_content('''Hello last time''')

#setting up server
server='smtp.gmail.com'
port=587

#login credentials
email='chandrayanpaul27@gmail.com'
password='tnnp hkzm pulr jxvx'

#sending the mail
with smtplib.SMTP(server,port) as server:
    server.starttls()
    server.login(email,password)
    server.send_message(msg)

print("email sent successfully!!")