#!/usr/bin/python2

import time
import webbrowser
import requests as req
from bs4 import BeautifulSoup as BS
import os

option='''
Press  1 :  Enter anything - split each word and search on google
Press  2 :  Enter anything - split each word but find images as answers 
Press  3 :  Enter anything - split each word and find URL of each result
Press  4 :  Current time and date
Press  5 :  Open default browser
Press  6 :  All Network IPs
Press  7 :  Enter domain name and find owner, email & contact
'''
print  option

ch=raw_input()

if   ch ==  '1'  :
	search_data=raw_input("Enter data to search: ")
	final_data=search_data.strip()
	#  above removing  leading and trailing space 

	done_data=final_data.split()
        #  spliting each word by space
 
	for  i  in  done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif ch == '2'  :
	
	search_data=raw_input("Enter data to search images: ")	
	final_data=search_data.strip()

	done_data=final_data.split()

	for i in done_data:
		webbrowser.open_new_tab('https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1366&bih=596&ei=mswHW9eVNoiCvQSH_IrQCA&q='+i)

elif ch == '3'  :
	
	search_data=raw_input("Enter data to find all urls: ")
	url = "https://www.google.com/search?q=" + search_data
	page = req.get(url)
	s = page.text
	soup = BS(s,'html.parser')

	q = soup.find_all('a')
	#print(q) 
	#print(soup.prettify())

	for link in soup.find_all('a'):
  		print(link.get('href'))


elif ch == '4'  :
	print time.ctime()


elif ch == '5'  :
	webbrowser.get('firefox').open_new_tab('')

elif ch == '6'  :
	os.system("ifconfig | grep -i inet | awk -F ' ' '{print $2}' ")


elif ch == '7'  :
	search_data=raw_input("Enter domain to get info: ")
	os.system("whois "+search_data)


else :

	print  "no chance !!"

