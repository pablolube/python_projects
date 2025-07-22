import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Tu email y contraseña de aplicación (no tu contraseña real), esto lo haces desde la configuracion 'contraseñas para aplicaciones'
your_email = 'pablolube@gmail.com'
your_password = 'contra_app'  # Contraseña de aplicación de Gmail

# Destinatario
recipient = 'pablolube@gmail.com'

# Crear el mensaje
message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipient
message['Subject'] = 'Email de prueba'
body = 'Esta es una prueba.'
message.attach(MIMEText(body, 'plain')) 

# Enviar el correo usando el servidor SMTP de Gmail
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Especificar host y puerto
    smtp_server.starttls()  
    smtp_server.login(your_email, your_password) #loggueo
    smtp_server.sendmail(your_email, recipient, message.as_string()) #creo mensaje
    smtp_server.quit() # salir del server 
    print('Email enviado correctamente.')
except Exception as e:
    print(f'Error al enviar el email: {e}')
