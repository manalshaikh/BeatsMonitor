##################################################
# By Manal Shaikh (github.com/ManalShaikh) and big thanks to the random Stackoverflow dude asking questions from 2009 to 3 weeks ago.
# Sorry not sorry for the messy code. 
# Of course I am not responsible for whatever you do with this. Pls dont do anything illegal or bad. Read the license for more info.
# Credits are more than appreciated in any environment.
# If you want to support me and the project, you can donate me through the donation button in README.md(repo descripiton) or you can
# ..-simply buy a secure & affordable VPS from ShadowHosting.net/vps-hosting.html starting from just $8.00/month for 4GB-80GBHDD-1vCore VPS.
# The IP address that you will be provided is clean from all kinds of blacklisting, hence, best for SMTP/emailing. On the other hand,
# ..-it can handle heavy loads and you will be contributing to the project at the same time :). 
# Open a ticket and give reference of this repo to get additional 15% OFF(after coupon) on your first purchase of a VPS server of any category.
##################################################
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import time
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
import mysql.connector
import sys

a1 = sys.argv[1]
ehost = 'email.shadowhosting.net' # Your mailserver hostname / IP address here.
user = 'indar@shadowhosting.net' # Your email ID / username for SMTP authentication here. (pls buy)
password = 'gratchal53' # Yes, zuk. im trolling you.

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

#Beginning of MySQL function
def dbSelect(serverid):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="beatsmonitor") # My localhost xampp details. will leave it here.
    mycursor = mydb.cursor()
    query = "SELECT * FROM servers WHERE serverid = " + str(serverid) + ";" # Idk what I did here. But somehow it worked. Improvements are appreciated. You can open issues in the repo.
    print(query)
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def fetchIP():
    a1 = sys.argv[1]
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="beatsmonitor")
    mycursor = mydb.cursor()
    query = "SELECT hostname FROM servers WHERE serverid = " + a1 +";"
    mycursor.execute(query)
    result = mycursor.fetchone()
    for x in result:
        x
    return x

def dbUpdate(status, serverid):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="beatsmonitor")
    mycursor = mydb.cursor()
    query = "UPDATE servers SET status = '" + str(status) +"' WHERE serverid = " + serverid + ";"
    mycursor.execute(query)
    mydb.commit()
#End of MySQL function

def ChkOnline(): # Test IP to deilberately show that the website is down.
    t = ping(fetchIP())
    if t == True:
        print("Site is online")
        dbUpdate("Online", a1)
    else:
        print("Site is offline")
        dbUpdate("Offline", a1)
        sender = user
        receiver = 'manal@shadowhosting.net' # Receiver's email where it is to be alerted. Yea, my company email.
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