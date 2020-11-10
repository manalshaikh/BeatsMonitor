from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import time
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

# Beginning of ping function
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0
# End of ping function

ehost = 'buy.from.shadowhosting.net' # Your mailserver hostname / IP address here.
user = 'buy@shadowhosting.net' # Your email ID / username for SMTP authentication here. (pls buy)
password = 'plsbuyfromshadowhostingsothaticansupportthisproject' # Your password here.



def ChkOnline():
    ip = "myserver.shadowhosting.net" # Test IP to deilberately show that the website is down.
    t = ping(ip)
    if t == True:
        print("Site is online")
    else:
        print("Site is offline")
        sender = user
        receiver = 'selfmail@googlemailorwhateveryouwishhere.com' # Receiver's email where it is to be alerted.
        now = datetime.now()
        msg = MIMEText('Your server was unpingable and assumed down at ' + now.strftime('%H:%M:%S - %d/%m/%Y' '. We will check again after 5 minutes. '))

        msg['Subject'] = 'DOWN! Your website is down.' 
        msg['From'] = user
        msg['To'] = receiver


        with smtplib.SMTP(ehost, 587) as server:
            server.starttls()
            server.login(user, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("mail successfully sent")  
ChkOnline()