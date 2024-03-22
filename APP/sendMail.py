import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(student,receiver,link):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'roeverbonafide@gmail.com'
    SMTP_APP_PASSWORD = 'krlq lemj jzzt poow'
    link = f"https://localhost:8000/media/{link}"
    msg = MIMEMultipart()
    msg['From'] = 'roeverbonafide@gmail.com'
    msg['To'] = f'{receiver}'
    msg['Subject'] = 'Bonafide Request Accepted'

    body = f"Hello {student}. this is download link for  your certificate bonafide certificate :  {link} . If the link is not working please visit your dashboard"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_APP_PASSWORD)


    server.sendmail(SMTP_USERNAME, receiver, msg.as_string())


    server.quit()
