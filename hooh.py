import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


with open('password.txt','r') as f:
    password = f.read()


me = "alicesingh19@gmail.com"

my_password = password

you = "rojina.hengaju19@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Message from a Bot"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hello Maam! How was your date???</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
filename = 'meme.jpeg'
attachment = open(filename,'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)

s = smtplib.SMTP_SSL('smtp.gmail.com')

s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()