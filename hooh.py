import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#add your gmail here
me = "yourgmailhere.com"
my_password = r"your password here"

client = "client'sgmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Message from a Bot"
msg['From'] = me
msg['To'] = client

html = '<html><body><p> Place your message here </p></body></html>'
message = MIMEText(html, 'html')
msg.attach(message)


# Uncomment this if you want to send an image or file with the message above to the client

# filename = 'meme.jpeg'
# attachment = open(filename,'rb')

# p = MIMEBase('application','octet-stream')
# p.set_payload(attachment.read())

# encoders.encode_base64(p)
# p.add_header('Content-Disposition',f'attachment;filename={filename}')
# msg.attach(p)

s = smtplib.SMTP_SSL('smtp.gmail.com')

s.login(me, my_password)

s.sendmail(me, , msg.as_string())
s.quit()
