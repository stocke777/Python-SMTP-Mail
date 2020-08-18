import smtplib
from email import encoders
from email.mime.text import MIMEText    
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  #make the server and add (Host, Port) as u like
server.connect("smtp.gmail.com",465)  #connect the server
server.ehlo()  

password = ""  #use google app password here, better to save it on a different text file and open it her or use Environment Variables

server.login('deshwaljaivardhan@gmail.com', password)  #login using your credentials

msg = MIMEMultipart()   #set mail variables here
msg['From'] = 'Jai'
msg['To'] = 'vcl29778@cuoly.com'
msg['Subject'] = "Just a Test 1"

message = "this is JUST testing out the script"  # mail body

msg.attach(MIMEText(message, 'plain'))  #plain text format

filename = 'photo.jpg'   #add image name in the directory
attachment = open(filename, 'rb')  # open it as bytes as its an image

p = MIMEBase('application', 'octet-stream')  # dunno, what it does
p.set_payload(attachment.read())

encoders.encode_base64(p)  
p.add_header('Content-Disposition', f'attachment; filename = {filename}') #just adding header
msg.attach(p) #attach image to mail
text = msg.as_string() 

server.sendmail('deshwaljaivardhan@gmail.com', 'example@gmail.com', text)
del msg
server.quit()
