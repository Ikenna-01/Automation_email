import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(recipient, subject, body):
    senderemail = "support@learnfinity.co.uk"
    password = "mljcoyrswdajpuyt"
    message = MIMEMultipart()
    message['From'] = senderemail
    message['To'] = recipient
    message['subject'] = subject

    message.attach(MIMEText(body,'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587) #establishing the host of the recipient
    session.starttls() # establishes a secure connection to the server
    session.login(senderemail, password)
    text = message.as_string() #converts message into string
    session.sendmail(senderemail, recipient, text)
    session.quit()


send_email('ikenna.okorafor@gmail.com', 'test', 'this is a test email')