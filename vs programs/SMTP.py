import smtplib

sender = "kingpathu26@gmail.com"
receiver = "parthchotaliya788@gmail.com"
password = "P@artH2005"
smtpserver = smtplib.SMTP("gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(sender,password)
msg = 'Subject : Tesing\n "Hello Part,\n This is just for testing...'
smtpserver.sendmail(sender,receiver,msg)
print('sent')
smtpserver.close()