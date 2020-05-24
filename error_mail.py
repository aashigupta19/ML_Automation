import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


mail_content = '''For Developer,
This is to inform your that the model cannot be loaded correctly for training due to some errors in the code. You are requested to look into the model and rectify the code soon.
Thank You! :)
' ' '

#The mail addresses and password
sender_address = 'coding548@gmail.com'
sender_pass = '1234coding'
receiver_address = 'aashi.gupta6477@gmail.com'


#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Failure of model for Training due to error in code'   #The subject line


#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))


#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security

session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()

session.sendmail(sender_address, receiver_address, text)
print("error mail sent")
session.quit()
