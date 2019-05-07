# Python code to illustrate Sending mail
# to multiple users
# from your Gmail account
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# list of email_id to send the mail
li = ["EmergencyDistressSignal223@gmail.com", "tbramlet@uccs.edu"]

email = "EmergencyDistressSignal223@gmail.com"
password = str(input("\nENTER PASSWORD >> "))
send_to_email = 'EmergencyDistressSignal223@gmail.com@gmail.com'
subject = "+++ TEST MESSAGE +++"
message = "THIS IS ONLY A TEST ..."

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

for i in range(len(li)):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, li[i], text)
server.quit()

# EMERGENCY LOCATOR
# EmergencyDistressSignal223@gmail.com
# safe556Distress!
