import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.ebay.com/itm/Pokemon-Cards-XY-Fates-Collide-Booster-Pack-10-cards-New-Factory-Sealed/362633593734?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3Db58752b1216344db92dd2952695b8266%26pid%3D100675%26rk%3D1%26rkt%3D15%26sd%3D362633593734%26itm%3D362633593734%26pg%3D2481888&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Aed48b66f-a4d7-11e9-9026-74dbd1804f18%7Cparentrq%3Ae792e2d916b0a68d5f8c3c30ff824a02%7Ciid%3A1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jaxlombard@gmail.com', 'odrcpvvbumhxvart')

    subject = 'Price fell down!'
    body = 'Check the link! https://www.ebay.com/itm/Pokemon-Cards-XY-Fates-Collide-Booster-Pack-10-cards-New-Factory-Sealed/362633593734?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3Db58752b1216344db92dd2952695b8266%26pid%3D100675%26rk%3D1%26rkt%3D15%26sd%3D362633593734%26itm%3D362633593734%26pg%3D2481888&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Aed48b66f-a4d7-11e9-9026-74dbd1804f18%7Cparentrq%3Ae792e2d916b0a68d5f8c3c30ff824a02%7Ciid%3A1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender@gmail.com',
        'reciever@gmail.com',
        msg
    )

    server.quit()
def check_price():
    price = soup1.find(id="prcIsum").get_text()
    converted_price = float(price[4:5])
    if (converted_price < 5.00):
        send_mail()

while (True):
    check_price()
    time.sleep(86400) #one day
    

