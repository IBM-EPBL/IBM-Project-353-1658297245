import smtplib

from email.mime.text import MIMEText

def send_mail(name,phone_number,email,feedback):
  sender=email
  receiver='trj08012002@gmail.com'
  message=f"""\
  Subject: Hi TDLH
  From: {sender}
  To: {receiver}
  Name: {name}
  Phone number: {phone_number}
  Feedback: {feedback}"""
  msg = MIMEText(message)
  msg['Subject'] = "Feedback"
  msg['From']    = sender
  msg['To']      = receiver
  s = smtplib.SMTP('smtp.mailgun.org', 587)
  s.login('postmaster@sandboxd7f36f8c295b489fa32bbb5e3f831f50.mailgun.org', '440b7d4f8713fc5a46cb6cbb263b9849-48c092ba-2004824a')
  s.sendmail(msg['From'], msg['To'], msg.as_string())
  s.quit()
  
