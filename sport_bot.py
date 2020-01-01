#always restart  after some minutes
import requests
from bs4 import BeautifulSoup
import fbchat
from fbchat import Client
import time
s = [ 1]
url_r =("https://www.sportinglife.com/football/live/vidiprinter")
URL = url_r
headers = {"user-agent" : 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(class_ = "vidiprinter-title").get_text()
date = soup.find(class_ = "full-date").get_text()
    #print (date)
a = soup.find_all(class_ = "vidiline-link")
    #print (a)
for obj in a:
    a=(obj.get_text())
    print (a)
    s.append(a)

def fb_bot():
    client = fbchat.Client('username','Password')
    no_of_friends = int(1)
    for I in range(no_of_friends):
        name = "name of friend to message"
        friends = client.searchForUsers(name)
        friend = friends [0]
        while True:
            for obj in s:
                for i in range (len(s)):
                    print (i)
                    msg =(s[-1] + "\n" + "\n")
                    msg+=(s[-2] + "\n" + "\n")
                    msg+=(s[-3] +  "\n" + "\n")
                    msg+=(s[-4]  + "\n" + "\n")
                    msg+=(s[-5]  + "\n" + "\n")
                    msg+=(s[-6]  + "\n" + "\n")
                    msg+=(s[-7]  + "\n" + "\n")
                    msg+=(s[-8]  + "\n" + "\n")
                    msg+=(s[-9]  + "\n" + "\n")
                    msg+=(s[-10]  + "\n" + "\n")
                    msg+=(s[-11]  + "\n" + "\n")
                    msg+=(s[-12]  + "\n" + "\n")
                    msg+=(s[-13]  + "\n" + "\n") 
                    msg+=(s[-14]  + "\n" + "\n")
                    msg+=(s[-15]  + "\n" + "\n")
                    sent = client.sendMessage(msg,thread_id=friend.uid)
                    if sent:
                        ("message sent")
                        time.sleep(120)
                    else:
                        break
fb_bot()







"""# Python code to demonstrate the working of 
# sleep() 

  
#  importing "time" module for time operations 

import time 

  
# using ctime() to show present time 

print ("Start Execution : ",end="") 

print (time.ctime()) 

  
# using sleep() to hault execution 

time.sleep(4) 

  
# using ctime() to show present time 

print ("Stop Execution : ",end="") 

print (time.ctime())"""
    