import imaplib
import email
from email.header import decode_header, make_header
#This code is only for daum.net

def imap_daum(id, pw, num_mails): # 메일의 갯수()
    server = imaplib.IMAP4_SSL('imap.daum.net')
    server.login(id, pw)
    rv, data = server.select()
    recent_no = data[0]

    # [][0]:date [][1]:발신자 [][2]:제목
    mailList = [] # 메일의 결과 리스트
    
    for i in range(num_mails):
        mail_no = str(int(recent_no.decode('utf-8'))- i).encode('utf8')
        rv, fetched = server.fetch(mail_no, '(RFC822)')
        message = email.message_from_bytes(fetched[0][1])

        date = make_header(decode_header(message.get('Date')))
        fr = make_header(decode_header(message.get('From')))
        subject = make_header(decode_header(message.get('subject')))

        mailList.append([date,fr,subject])
    return mailList