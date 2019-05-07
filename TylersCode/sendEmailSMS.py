# Python code to illustrate Sending mail  
# to multiple users  
# from your Gmail account  
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# list of email_id to send the mail 
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] 

email = 'xxxx@gmail.com'
password = str(input("\nENTER PASSWORD >> "))
send_to_email = 'xxxx@gmail.com'
subject = "EMERGENCY DISTRESS"
message = 'ALERT!!!'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()# You now need to convert the MIMEMultipart object to a string to send
server.sendmail(email, send_to_email, text)
server.quit()
