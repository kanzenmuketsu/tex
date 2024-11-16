import smtplib
import local_settings # added to .gitignore.
from random import randint
from smtplib import SMTPResponseException




CODES ={}

def send_email_code(id: str, to_address: str):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    smtpObj.starttls()
    code = str(randint(500000, 999933) + int(id))
    # from env file
    email_address = local_settings.EMAIL_ADDRESS
    email_password = local_settings.EMAIL_PASSWORD

    smtpObj.login(email_address,email_password)
    try:
        smtpObj.sendmail(email_address, to_address, code)
    except SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        print(error_code)
        print(error_message)
    else:
        CODES[id] = code
    finally:
        smtpObj.quit()
        print(CODES)