#!/usr/bin/python

import os
import subprocess
import socket


#Updating the packages
subprocess.call(["sudo","apt-get","update","-y"])

subprocess.call(["sudo","apt-get","upgrade","-y"])


#Installing samba and CUPS the Print Server
subprocess.call(["sudo","apt-get","install","samba","-y"])

subprocess.call(["sudo","apt-get","install","cups","-y"])

subprocess.call(["sudo","apt-get","install","hplip","-y"])

subprocess.call(["sudo","usermod","-a","-G","lpadmin","pi"])

subprocess.call(["sudo","cupsctl","--remote-any"])

subprocess.call(["sudo","/etc/init.d/cups","restart"])


#For Airprint functionality
subprocess.call(["sudo","apt-get","install","avahi-discover","-y"])


#Disable power saving - it is a PiZero
os.system("sudo echo 'options 8192cu rtw_power_mgnt=0 rtw_enusbss=1 rtw_ips_mode=1' >> 8192cu.conf")

os.system("sudo mv 8192cu.conf /etc/modprobe.d/")



print("Install complete!")

#Getting PrintServer IP Address
ip_address = socket.gethostbyname(socket.gethostname())

print("I recommend you add update the packages on your Print Server regular below are directions on how to run updates every Sunday")

print("Run 'crontab -e' then add below two lines:\n \t 0 0 * * SUN sudo apt-get update -y \n \t 0 1 * * SUN sudo apt-get upgrade -y" )

print("Go to https://" + ip_address + ":631/admin to add your printer you can login with pi user's credentials")

