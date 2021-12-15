#!/usr/bin/env python3
from earnapp import earnapp
import time

user = earnapp.User()
loggedIn = user.login("oauth-refresh-token")

# file contain sdk node
file = open('earnapp.txt', "r")
# read file
lines = file.readlines()
# close the file
file.close()
if loggedIn == True: 
   print("Successfully logged in!")
   for line in lines: #browse file line after line , strip revoce space
       print(user.linkDevice(line.strip()))
       time.sleep(120) #add timer for antispam website in second
else:
   print("Failed to log in")

