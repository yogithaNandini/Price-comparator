from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def paytmMallMOBILE(key):
    for x in range(1,3):
        my_url ='https://paytmmall.com/shop/search?q=mobiles&from=organic&child_site_id=6&site_id=2&category=6224&page='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("div",{"class":"_2apC"})
        container1 = page_soup.findAll("div",{"class":"_1kMS"})
        for i in range(len(container)):
            if(key==container[i].text.split(" ")[0]):
                print("Paytm Mall Product:",container[i].text)
                print("Paytm Mall price:",container1[i].text)
            else:
                pass
            
def paytamMallTV(key):
    for x in range(1,3):
        my_url='https://paytmmall.com/shop/search?q=televisions&from=organic&child_site_id=6&site_id=2&category=24843&page='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("div",{"class":"pCOS"})
        container1 = page_soup.findAll("div",{"class":"_1kMS"})
        for i in range(len(container)):
            if(key==container[i].text.split(" ")[0]):
                print("Paytm Mall Product:",container[i].text)
                print("Paytm Mall price:",container1[i].text)
            else:
                pass

def flipkartMOBILE(key):
    for x in range(1,6):
        my_url ='https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("div",{"class":"_1-2Iqu row"})
        container1 = page_soup.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
        for i in range(len(container)):
            if(key==container[i].div.div.text.split(" ")[0]):
                print("Flipkart Product:",container[i].div.div.text)
                price = [container1[i].text]
                print("Flipkart price:",price[0][1:])
            else:
                pass
def flipkartTV(key):
    for x in range(1,3):
        my_url ='https://www.flipkart.com/search?q=TV&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("div",{"class":"_1-2Iqu row"})
        container1 = page_soup.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
        for i in range(len(container)):
            if(key==container[i].div.div.text.split(" ")[0]):
                print("Flipkart Product:",container[i].div.div.text)
                price = [container1[i].text]
                print("Flipkart price:",price[0][1:])
            else:
                pass

def eBayMOBILE(key):
    for x in range(1,3):
        my_url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=mobiles&_sacat=0&_pgn='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("h3",{"class":"s-item__title"})
        container1 = page_soup.findAll("span",{"class":"s-item__price"})
        for i in range(len(container)):
            if(key==container[i].text.split(" ")[0]):
                print("EBay Product:",container[i].text)
                print("EBay price:",container1[i].text)
            if(key!=container[i].text.split(" ")[0]):
                pass

def eBayTV(key):
    for x in range(1,3):
        my_url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=tv&_sacat=0&_pgn='+str(x)
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = page_soup.findAll("h3",{"class":"s-item__title"})
        container1 = page_soup.findAll("span",{"class":"s-item__price"})
        for i in range(len(container)):
            if(key==container[i].text.split(" ")[0]):
                print("EBay Product:",container[i].text)
                print("EBay price:",container1[i].text)
            else:
                pass

cat = input("Enter Category:")
if(cat=="Mobiles"):
    key = input("Enter Product Name:")
    flipkartMOBILE(key)
    paytmMallMOBILE(key)
    eBayMOBILE(key)
if(cat=="TV"):
    key = input("Enter Product Name:")
    flipkartTV(key)
    paytamMallTV(key)
    eBayTV(key)
