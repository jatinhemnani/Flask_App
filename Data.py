from bs4 import BeautifulSoup
import requests
import re

# PRODUCT Realme X (Space Blue, 128 GB)  (4 GB RAM) START
url = "https://bit.ly/3ezbogK"
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, "html.parser")



###############
# FUNCTION FOR TITLE
###############
def title(soup):
    
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item

# FUNCTION FOR PRICE
def price(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item 

# FUNCTION FOR RATINGS
def rating(soup):
    # soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find("h1", class_="_9E25nV").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item
###############
# PRODUCT Realme X (Space Blue, 128 GB)  (4 GB RAM) END
###############

###############
#PRODUCT 2 START
###############
url1 = "https://bit.ly/3hcEZy1"
r1 = requests.get(url1)
html_content1 = r1.content
soup1 = BeautifulSoup(html_content1, "html.parser")        
        
def title1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating1(soup1):
    
    title = soup1.find("h1", class_="_9E25nV").get_text()
    price = soup1.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup1.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 2 END
###############


###############
#PRODUCT 3 START
###############
url2 = "https://bit.ly/2Cri2si"
r2 = requests.get(url2)
html_content2 = r2.content
soup2 = BeautifulSoup(html_content2, "html.parser")        
        
def title2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating2(soup2):
    
    title = soup2.find("h1", class_="_9E25nV").get_text()
    price = soup2.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup2.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 3 END
###############

###############
#PRODUCT 4 START
###############
url3 = "https://bit.ly/2ODtWSr"
r3 = requests.get(url3)
html_content3 = r3.content
soup3 = BeautifulSoup(html_content3, "html.parser")        
        
def title3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating3(soup3):
    
    title = soup3.find("h1", class_="_9E25nV").get_text()
    price = soup3.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup3.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 4 END
###############


###############
#PRODUCT 5 START
###############
url4 = "https://bit.ly/3hiXykh"
r4 = requests.get(url4)
html_content4 = r4.content
soup4 = BeautifulSoup(html_content4, "html.parser")        
        
def title4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating4(soup4):
    
    title = soup4.find("h1", class_="_9E25nV").get_text()
    price = soup4.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup4.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 5 END
###############



###############
#PRODUCT 6 START
###############
url5 = "https://bit.ly/2OTwgVD"
r5 = requests.get(url5)
html_content5 = r5.content
soup5 = BeautifulSoup(html_content5, "html.parser")        
        
def title5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[0:1]:
        return item        

def price5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[1:2]:
        return item   

def rating5(soup5):
    
    title = soup5.find("h1", class_="_9E25nV").get_text()
    price = soup5.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    rating = soup5.find("div", class_="hGSR34").get_text()
    data=title, price, rating
    for item in data[2:3]:
        return item         
###############
#PRODUCT 6 END
###############