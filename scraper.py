import requests
from bs4 import BeautifulSoup
import smtplib
import time




# location of product on website
URL = "https://www.amazon.in/dp/B07XG2KHCN/ref=pc_mcnc_merchandised-search-16_?pf_rd_s=merchandised-search-16&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=X7DDT9VBESFJM7KP0X84&pf_rd_p=d736bd91-d2f4-4e41-b555-380e3a96f61f"

# Contains information about web browser

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def check_price():
   while True:
        try:
            page = requests.get(URL, headers = headers)
            time.sleep(3)
        except:
            continue
    
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[-9:].replace(",",""))
    

    print(title.strip())

    print(converted_price)
    if converted_price < 25000.00:
        send_mail()


def send_mail():
# Creating a connection with gmail
    server = smtplib.SMTP('smtp.gmail.com',25)
    server.connect('smtp.gmail.com',443)
# ehlo command - sent by one email server to another to indentify itself to create connection
    server.ehlo()   
# encrypting our connection
    server.starttls
    server.ehlo()
# logged in to gmail
    server.login('r.madhur000@gmail.com','umaobijytddddqfb')
    subject = "You are now relatively rich!!!"
    body = "Go to the following link- https://www.amazon.in/dp/B07XG2KHCN/ref=pc_mcnc_merchandised-search-16_?pf_rd_s=merchandised-search-16&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=X7DDT9VBESFJM7KP0X84&pf_rd_p=d736bd91-d2f4-4e41-b555-380e3a96f61f"
    msg = f"Subject: {subject}\n\n\n{body}"

    server.sendmail(
        'r.madhur000@gmail.com',
        'madhur_r@ph.iitr.ac.in',
        msg
    )
    server.quit()
check_price()
