#import requests, import web scraper, import gmail connection

import requests
from bs4 import BeautifulSoup
import smtplib 
import time 
from urllib.request import urlopen
from mailer import Mailer
from conversion import Conversion

#fucntion for prices, price conversion, title, and email
def get_price():
    URL = 'https://www.etsy.com/au/listing/731261963/dr-phil-earrings?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=dr+phil&ref=sr_gallery-1-3&organic_search_click=1&pro=1'
    page = urlopen(URL)
    soup = BeautifulSoup(page.read(), "html.parser")
    #Title of Product - Dr Phil Earrings
    print("**************************************************")
    title = (soup.find("h1", {"data-listing-id": "731261963"}))
    print(title.text.strip())
    price = soup.find("p", {"class": "wt-text-title-03 wt-mr-xs-2"})
    #remove white space from price
    price = str(price.text.strip())
    #converting price from string to float
    converted_price = Conversion.convert_price(price)
    #converting price from string to float
    print(converted_price)
  
    
    if(converted_price < 11.50):
        subject = 'Dr Phil earrings - price has fallen'
        body = 'The price of the Dr Phil earrings has fallen - check the etsy link! https://www.etsy.com/au/listing/731261963/dr-phil-earrings?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=dr+phil&ref=sr_gallery-1-3&organic_search_click=1&pro=1'
        Mailer.send_mail(subject, body)
    else:
        print("Price is above $11.50 - no email sent :-(")

#get_price()
 

class Time_mod:
    while(True):
        get_price()
        time.sleep(60 * 60)
    #will check price once a day
    #call fucntion
    
get_price()
########