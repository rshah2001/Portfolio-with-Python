import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "rishil13123@gmail.com"
password = "lkiwaktwxjxutjom"

receiver = "rishilshah1211@gmail.com"
context = ssl.create_default_context()


message = """\
Subject: Test
hi!
How are you?
bye!
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
