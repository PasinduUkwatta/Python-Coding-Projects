import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Pasindu Ukwatta'
email['to'] = 'pasinduukwatta96@gmail.com'
email['subject'] = 'Test Email Send from Python'

email.set_content(html.substitute({'name':'pasindu'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # starting the smtp
    smtp.ehlo()
    # this is an encryption method
    smtp.starttls()

    smtp.login("deshan96.uom@gmail.com", "yqvgyfhahwirupgl")
    smtp.send_message(email)
    print('all done')


