
import smtplib,time
from email.message import EmailMessage
def send_email(sender,password,to_addr,subject,body,attachment_path=None):
    msg=EmailMessage()
    msg["From"]=sender; msg["To"]=to_addr; msg["Subject"]=subject
    msg.set_content(body)
    if attachment_path:
        with open(attachment_path,"rb") as f:
            data=f.read()
        msg.add_attachment(data,maintype="application",subtype="pdf",filename="resume.pdf")
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(sender,password)
        s.send_message(msg)
