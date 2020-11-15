##################################################
# By Manal Shaikh (github.com/ManalShaikh)
# Design credit AdminLite v3(Google up)
# Sorry not sorry for the messy code. 
# Of course I am not responsible for whatever you do with this. Pls dont do anything illegal or bad. Read the license for more info.
# Credits are more than appreciated in any environment.
# Note - This mysqltest.py is completely useless. I use this for testing so if incase this gets uploaded, don't take it seriously.
##################################################
import mysql.connector
import sys
import subprocess
import platform

a1 = sys.argv[1]

def dbSelect(serverid):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="beatsmonitor")
    mycursor = mydb.cursor()
    query = "SELECT * FROM servers WHERE serverid = " + str(serverid) + ";"
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

#ip = fetchIP()
#print(fetchIP())
#fetchIP()
#print(ping(fetchIP()))
#myip = fetchIP()
#print(fetchIP())
#print(ping('1.1.1.1'))
#print(ping(fetchIP()))