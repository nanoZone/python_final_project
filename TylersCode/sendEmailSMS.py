# Python code to illustrate Sending mail
# to multiple users
# from your Gmail account
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(signal, emailList):
    # list of email_id to send the mail
    li = ["EmergencyDistressSignal223@gmail.com"]
    newEmail = str(input("\nENTER AN EMAIL ADDRESS >> "))
    li.append(newEmail)

    email = "EmergencyDistressSignal223@gmail.com"
    password = str(input("\nENTER SERVER PASSWORD >> "))
    send_to_email = 'EmergencyDistressSignal223@gmail.com'
    subject = "+++ TEST MESSAGE +++"
    message = signal

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

content = "I am safe, this is a test message for our final project ..."
sendEmail(content)
