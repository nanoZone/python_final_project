# Python code to illustrate Sending mail  
# to multiple users  
# from your Gmail account  
import smtplib 
  
# list of email_id to send the mail 
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("sender_email_id", "sender_email_id_password") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", li[i], message) 
    s.quit() 
