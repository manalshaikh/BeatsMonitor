# BeatsMonitor
Beats Monitor is a server uptime monitoring application. If a server stops pinging, it sends an email to you. It is currently in it's early development. There are many plans for it to be implemented.
# Features
 - Sends an email whenever the server is down.
 - Easy configuration for outgoing mailing with TLS connection.

More features to come soon!

# Installation and Setup
Due to the script being in early development, we will use cron to keep it in rotation. 
Save the below-written script in */etc/cron.d/yourfilenamehereanythingrandom.cron*.
```
# run script every 5 minutes
*/5 * * * *   root  python3 /root/monitor.py

# run script after system (re)boot
@reboot       root  python3 /root/monitor.py
```

# How to use?
Before you start using it, you need a python library which can be easily installed using pip command. Use the following command to begin with installation of "pythonping".

`pip install pythonping`

Once done, you can now start using the script. Make sure the user is root/admin to begin as pythonping can only ping if the executing user has system permissions.

`python monitor.py`

It will take upto 15 seconds to check. If the given IP is online, it will say it's online otherwise it will send an email. 
# Email Server
You can use Google's SMTP server which uses your email to send outgoing emails. Hostname is smtp.google.com, username and password is your email and it's login password which you use in gmail.com. 

You can also buy a VPS from https://shadowhosting.net/vps-hosting.html and setup an email server, truly your own mail server. Refer this repository after ordering this server in support ticket and get free Mailcow installation in your VPS.
