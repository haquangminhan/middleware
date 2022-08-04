# import smtplib

# smtp_server = "smtp.gmail.com"
# port = 465

# def send(email, password, reciever, message):
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.login(email, password=password)
#         server.sendmail(email, reciever, message)


# if(send("haquangminhan@gmail.com","uvwtasilkyomtwcw","un66967@gmail.com","Hello")):
#     print("Successful!")
    # email = 'haquangminhan@gmail.com'
    # password = 'uvwtasilkyomtwcw'
    # reciever = 'un66967@gmail.com'
import smtplib
def send(email, password, subject, body,reciever):
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (email, ", ".join(reciever), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(email, password )
        smtp_server.sendmail(email, reciever, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)
