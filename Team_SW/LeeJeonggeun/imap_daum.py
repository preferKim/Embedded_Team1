import imaplib
import email
from email.header import decode_header, make_header
#This code is only for daum.net
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
