import ssl, smtplib


def send_email(message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "Your Email Here"
    receiver_email= "Recipient Email Here"
    password = "Your Password Here"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server,port , context = context) as server:
        try:
            server.login(sender_email , password)
            res = server.sendmail(sender_email , receiver_email,message)
            print('Email Sent!')
        except :
            print("Could not login or send the mail :( .")

