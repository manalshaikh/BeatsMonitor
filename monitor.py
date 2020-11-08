from pythonping import ping # Required to be installed using `pip install pythingping` and only runs on root.
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
ehost = 'mail.youremailserver.here' # Your mailserver hostname / IP address here.
user = 'yourusername@mailprovider.here' # Your email ID / username for SMTP authentication here.
password = 'YourpAsswordhEre' # Your password here.

ip = "125.33.68.2" # Test IP to deilberately show that the website is down.
t = ping(ip)
if t == True:
    print("Site is online")
else:
    print("Site is offline")
    sender = 'yourusername@mailprovider.here'
    receiver = 'yourusername@gmail.com'
    now = datetime.now()
    msg = MIMEText('Your server was unpingable and assumed down at ' + now.strftime('%H:%M:%S - %d/%m/%Y.'))

    msg['Subject'] = 'DOWN! Your website is down.' 
    msg['From'] = user
    msg['To'] = receiver


    with smtplib.SMTP("email.server.here", 587) as server:
        server.starttls()
        server.login(user, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("mail successfully sent")