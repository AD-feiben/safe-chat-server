import smtplib
from email.mime.text import MIMEText
from email.header import Header

import config
from utils.my_exception import MyException, ErrorEnum


async def send_mail_async(*args, **kwargs):
    return send_mail(*args, **kwargs)


def send_mail(email, subject, msg, msg_type='plain'):
    receivers = [email]

    message = MIMEText(msg, msg_type, 'utf-8')

    message['From'] = Header(config.Mail['user'], 'utf-8')
    message['To'] = Header(email, 'utf-8')
    message['Subject'] = Header('【{}】'.format(config.App_Name) + subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP_SSL(config.Mail['host'], 465)
        smtp_obj.ehlo()
    except Exception as e:
        print(e)
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(config.Mail['host'], 25)

    try:
        smtp_obj.login(config.Mail['user'], config.Mail['pass'])
        smtp_obj.sendmail(config.Mail['user'], receivers, message.as_string())
    except Exception as e:
        print(e)
        raise MyException(ErrorEnum.MAIL_SEND_ERROR, e=e)
    finally:
        smtp_obj.quit()
