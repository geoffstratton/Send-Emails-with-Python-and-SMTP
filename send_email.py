import smtplib, string
from email import MIMEMultipart
from email import MIMEText
  
def mailer(strSender, lstEmailRecipients, strEmailSubject, strEmailBody):
    """Compose a message using arguments, pass it to MTA on server"""
  
    # add yourself for testing
    lstEmailRecipients.append('you@yourdomain.com')
  
    msg = MIMEMultipart.MIMEMultipart('alternative')
    msg['From'] = strSender
    #msg['To'] = lstEmailRecipients
    msg['Subject'] = strEmailSubject
  
    msgInHTML = """
    <html>
       <head></head>
       <body><font face="Arial">"""
    msgInHTML += strEmailBody
    msgInHTML += """
       </font></body>
    </html>"""
  
    msgPart1 = MIMEText.MIMEText(strEmailBody, 'plain', 'UTF-8')
    msgPart2 = MIMEText.MIMEText(msgInHTML, 'html', 'UTF-8')
  
    msg.attach(msgPart1)
    msg.attach(msgPart2)
  
    smtpserver = smtplib.SMTP("localhost")
    smtpserver.sendmail(msg['From'], lstEmailRecipients, msg.as_string())
    smtpserver.quit()