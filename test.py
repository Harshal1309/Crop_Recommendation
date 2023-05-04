import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your Gmail account credentials
gmail_user = 'hrjoshi13@gmail.com'
gmail_password = 'Pass@word@13'

# Create a message to send
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = 'joshiharshal13@gmail.com'
msg['Subject'] = 'Subject'

body = 'Body of your email'
msg.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

# Send the email
text = msg.as_string()
server.sendmail(gmail_user, 'joshiharshal13@gmail.com', text)
server.quit()
