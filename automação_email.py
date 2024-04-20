import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_user = 'seu_email@example.com'
smtp_password = 'sua_senha'

# Criando o e-mail
msg = MIMEMultipart()
msg['From'] = smtp_user
msg['To'] = 'destinatario@example.com'
msg['Subject'] = 'Assunto do E-mail'
corpo_email = 'Corpo do e-mail'
msg.attach(MIMEText(corpo_email, 'plain'))

# Enviando o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(msg)