import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender="da298017@gmail.com"
receiver=["wuwai628@outlook.com","da298017@gmail.com"]

for i in receiver:
    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"] =i
    header = Header("Test Send Email","utf-8")
    msg["subjeck"] = header.encode()

    body = "This is email send from python"
    msg.attach(MIMEText(body))
    ssl_context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"wbip pqgo mihv efsk")
        server.sendmail(sender,i,msg.as_string())
print("success send email")
