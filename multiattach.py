import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

From="maheshwari.t001@gmail.com"
code="mhbh apfi acly yeor"

server.login(From,code)
To="etikalasrinivas2345@gmail.com","maheshwarithangella@gmail.com","punnamvadai7@gmail.com"
subject="An Image"
matter="look at the image"

for user in To:
    msg=MIMEMultipart()
    msg["from"]=From
    msg["to"]=user
    msg["subject"]=subject



    msg.attach(MIMEText(matter))
    img= r"c:\Users\Mahi\Downloads\bedroom.jpg"
    file=open(img,"rb")
    attachment=MIMEBase("application","octet-stream")
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition","attachment", filename="home.png")
    
    msg.attach(attachment)
    print("done")
    
    server.sendmail(From,user,msg.as_string())
    print("success",user)

server.quit()