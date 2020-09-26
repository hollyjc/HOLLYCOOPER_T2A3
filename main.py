#import requests, import web scraper, import gmail connection

import requests
from bs4 import BeautifulSoup
import smtplib 
import time 
from urllib.request import urlopen

#URL of earrings on etsy
URL = 'https://www.etsy.com/au/listing/731261963/dr-phil-earrings?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=dr+phil&ref=sr_gallery-1-3&organic_search_click=1&pro=1'
#User-Agent of computer 
headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36' }

#fucntion for prices, price conversion, title, and email
def get_price():
    page = urlopen("https://www.etsy.com/au/listing/731261963/dr-phil-earrings?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=dr+phil&ref=sr_gallery-1-3&organic_search_click=1&pro=1")
    soup = BeautifulSoup(page.read(), "html.parser")
    #Title of Product - Dr Phil Earrings
    print("*************")
    title = (soup.find(id="731261963")
    #print("###############")
    print(title)
    price = soup.find(id="priceblock_ourprice").get_text()
    #converting price from string to float
    converted_price = float(price[1:5])
    
    if(converted_price > 13.00):
        send_mail()
    
    #Print product title - remove white space 
    print(title.strip())
    print(converted_price())
    
    if(converted_price > 13.00):
        send_mail()
        

get_price()
 
 #gmail connection, gmail connection number, encrypt server connection   
def send_mail():
    server = smtplib.SMTP('SMTP.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('hollyjanecooperr@gmail.com', 'pqqqzufgzqsybcni')
    
    subject = 'Dr Phil earrings - price has fallen'
    body = 'The price of the RM williams boots has fallen - check the etsy link! https://www.etsy.com/au/listing/731261963/dr-phil-earrings?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=dr+phil&ref=sr_gallery-1-3&organic_search_click=1&pro=1'
    
    msg = f" Subject{subject} \n\n{body} "
    
    server.sendmail(
        'hollyjanecooperr@gmail.com',
        'holly_cooper@live.com.au',
        msg
        )
    print('Email has been sent! :-)')
    
    #closing server connection
    server.quit()
    

class Time_mod:
    while(True):
        get_price()
        time.sleep(60 * 60)
    #will check price once a day
    #call fucntion
get_price()