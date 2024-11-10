import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
i = 1
fromGmail = "whatevergmailWantsToSendTheMessage"
toGmail = "whatevergmailWantsToReceiveTheMessgae" 
gmailSubject = "topicOfTheGmail"
tokenPassword = "TokenPasswordFromGoogle"

msg = MIMEMultipart()
msg['From'] = fromGmail
msg['To'] = toGmail
msg['Subject'] = gmailSubject
message = "Your Message goes here"
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(fromGmail, tokenPassword) #Login with your from email and also the token password

for i in range(999):
    i += 1
    mailserver.sendmail(fromGmail, toGmail,msg.as_string())
    print(f"Succesfully sent nr {i}")

mailserver.quit()