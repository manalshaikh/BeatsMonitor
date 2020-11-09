yum -y install git
yum -y install python3
echo "================"
echo "Successfully installed Git & Python. Beginning to install pythonping using pip3."
echo "================"
sleep 3
pip3 install pythonping
echo "================"
echo "Now open and edit monitor.py with your SMTP details before executing cron.sh"
echo "Make sure to edit beatsmon.cron with proper directory if not installed on /root/BeatsMonitor"
echo "================"