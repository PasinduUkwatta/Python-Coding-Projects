import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] ='Pasindu Ukwatta'
email['to'] = 'pasindu.17@itfac.mrt.ac.lk'
email['subject'] = 'Test Email Send from Python'

email.set_content('HI ! THIS IS A TEST PYTHON EMAIL GENRATED BY PYTHON CODING')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    #starting the smtp 
    smtp.ehlo()
    #this is an encryption method
    smtp.starttls()
    
    smtp.login("deshan96.uom@gmail.com","yqvgyfhahwirupgl")
    smtp.send_message(email)
    print('all done')
    

