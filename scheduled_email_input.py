import datetime as dt
import time
import smtplib
from email.mime.text import MIMEText



smtp_ssl_host = 'smtp.gmail.hu'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'your_login@gmail.com'
password = 'your_password'
smi = input("What's your sender mail? ")
sender = smi
tarm = input ("What is your target email address? ")
targets = tarm # for single target
#targets = ['firstmail@gmail.com', 'secondmail@gmail.com']

msginp = input ("What's your message? ")
msg = MIMEText(msginp)
msgsub = input ("What is your subject? ")
msg['Subject'] = msgsub
msg['From'] = sender
msg['To'] = targets # For single target 
# msg['To'] = ', '.join(targets) #for multipe target

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    print('email sent')


first_email_time = dt.datetime(2019,5,15,11,32,0) # set your sending time in UTC (2019/05/05,12:05:09 Should look like 2019,5,5,12,5,9)
interval = dt.timedelta(minutes=24*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()