import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.connect("smtp.gmail.com",465)
server.ehlo()

password = "aswlswaqvonmupat"

server.login('deshwaljaivardhan@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Jai'
msg['To'] = 'vcl29778@cuoly.com'
msg['Subject'] = "Just a Test 1"

message = "this is JUST testing out the script"

msg.attach(MIMEText(message, 'plain'))

filename = 'photo.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename = {filename}')
msg.attach(p)
text = msg.as_string()

server.sendmail('deshwaljaivardhan@gmail.com', 'vcl29778@cuoly.com', text)
del msg
server.quit()