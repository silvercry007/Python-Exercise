from bs4 import BeautifulSoup
import requests
from csv import writer

req = requests.get("https://magicpin.in/india/Pune/All/Spa/")

soup = BeautifulSoup(req.content, "html.parser")

lists = soup.find_all('div', class_="top-section")

with open('salonq.csv', 'w', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location']
    thewriter.writerow(header)
    
    for list in lists:
        title = list.find('h2', class_= "merchant-name").text.replace('\n', '')
        location = list.find('p', class_= "merchant-location").text.replace('\n', '')
        info = [title, location]
        thewriter.writerow(info)
    