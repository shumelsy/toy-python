'''
This script parses https://www.amazon.de site by URL and finds the price.
Then it sends email if the price is lower a definite value.
Optionally you need to pip install lxml lib
'''

from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.de/gp/product/B0756CYWWD/ref=as_li_tl?ie=UTF8&tag=idk01e-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B0756CYWWD&linkId=868d0edc56c291dbff697d1692708240'
header = {"User-agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}

def parser_price():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, "lxml") #Very fast
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(f'We are looking for the price of the product "{title.strip()}". Current price is {price}')
    price_converted = int(price.split(',')[0].replace('.', ''))
    if price_converted < 250:
        send_mail()
    else:
        print("Price is too high!")

def send_mail():
    server = smtplib.SMTP('mail.netangels.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sveta@XXXXXXX.ru', 'XXXXXXXXXXXXX')
    subject = "Hurry up! Prise is lower than 250!"
    body = f"Check the link: {URL}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'Price check',
        'sveta@XXXXXXXXX.ru',
        msg
    )
    print("E-mail has been sent")
    server.quit()

parser_price()

