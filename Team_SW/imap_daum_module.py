import imaplib
import email
from email.header import decode_header, make_header
#This code is only for daum.net

def imap_daum(id, pw, num_mails):
    server = imaplib.IMAP4_SSL('imap.daum.net')
    server.login(id, pw)
    rv, data = server.select()
    recent_no = data[0]

    mailList = []
    
    for i in range(num_mails):
        mail_no = str(int(recent_no.decode('utf-8'))- i).encode('utf8')
        rv, fetched = server.fetch(mail_no, '(RFC822)')
        message = email.message_from_bytes(fetched[0][1])

        date = make_header(decode_header(message.get('Date')))
        fr = make_header(decode_header(message.get('From')))
        subject = make_header(decode_header(message.get('subject')))

        mailList.append([date,fr,subject])
    return mailList

'''
mailList = imap_daum('', '', 20)

for i in range(len(mailList)):
    try:
        print(mailList[i][0], mailList[i][1], mailList[i][2])
    except:
        pass

ID = ''
PW = ''

server = imaplib.IMAP4_SSL('imap.daum.net')
server.login(ID, PW)

rv, data = server.select()
recent_no = data[0]

rv, fetched = server.fetch(recent_no, '(RFC822)')
message = email.message_from_bytes(fetched[0][1])

fr = make_header(decode_header(message.get('From')))
print(fr)

subject = make_header(decode_header(message.get('Subject')))
print(subject)
'''
