import datetime as dt
import time
import smtplib
from email.mime.text import MIMEText



smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'youremail@gmail.com'
password = 'Your_password'
sender = "Sender-mail"
targets = 'yourtaget@gmail.com' # for single target
#targets = ['firstmail@gmail.com', 'secondmail@gmail.com']

msg = MIMEText("Your message")
msg['Subject'] = "Subject"
msg['From'] = sender
msg['To'] = targets # For single target 
# msg['To'] = ', '.join(targets) #for multipe target

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    print('email sent')


first_email_time = dt.datetime(2019,5,17,9,0,0) # set your sending time in UTC
interval = dt.timedelta(minutes=24*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()