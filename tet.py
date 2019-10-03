import smtplib
import config


def sent_mail(sub, msg, to):
    try:
        sentmail = [to]
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        message = "Subject: {}\n\n{}".format(sub, msg)
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        print("authenticating......")
        server.sendmail(config.EMAIL_ADDRESS, sentmail, message)
        server.quit()
        print("Mail sent sucees")
    except:
        print("Unable sent mail")


sub = "YOUR LOGIN OTP"
msg = "OTP UNDER CONSTRUCTION"
print("Enter email address")
to = input()
sent_mail(sub, msg, to)
