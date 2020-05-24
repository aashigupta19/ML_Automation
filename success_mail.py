import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


mail_content = "For Developer, This is to inform you that model has achieved the desired accuracy and hencforth, will be used for further productions Thank You! :)"

#The mail addresses and password
sender_address = 'coding548@gmail.com'
sender_pass = '1234coding'
receiver_address = 'aashi.gupta6477@gmail.com@gmail.com'


#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Success of Model Training'   #The subject line


#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))


#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security

session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()

session.sendmail(sender_address, receiver_address, text)
print("success mail sent")
session.quit()
 
