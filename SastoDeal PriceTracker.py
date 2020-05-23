import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.sastodeal.com/'   #Insert Product URL

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)Gecko/20100101 Firefox/69.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", class_="name").get_text()
    price = soup.find("li", class_="mrp mrpPrice").get_text()
    price = price.replace(',','')
    converted_price = float(price[3:9])    #Convert String into Numbers

    if (converted_price < 25000):   #Desired User Price;
        print(title.strip())
        print(converted_price)
        send_mail()

def send_mail():	#Email Function
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender.xxxxx@gmail.com', 'password') 	#Email account to send mails

    subject = 'Price fell down on SastoDeal!!!'
    body = 'Check it out at' URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender.xxxxx@gmail.com',
        'reciever.xxxxx@gmail.com',  	#Designated Email
        msg
    )
    print('Your Email Has Been Sent!')		#Confirmation

    server.quit()


check_price()