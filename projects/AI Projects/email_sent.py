import smtplib

def sendEmail(email_receiver, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("pittarekha26@gmail.com", "Saisriram@2007")
    server.sendmail("pittarekha26@gmail.com", email_receiver, content)
    server.close()

email_receiver = input(str("Enter receiver's email: "))
content = input(str("Enter the content: "))
receive_process = sendEmail(email_receiver, content)

print(receive_process)
if receive_process:
    print("Email sent.")
