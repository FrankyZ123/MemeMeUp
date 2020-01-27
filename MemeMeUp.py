import requests
from bs4 import BeautifulSoup
import random
import webbrowser
import time
import sys

url = requests.get('https://funnyjunk.com/')

soup = BeautifulSoup(url.text, 'html.parser')

data = []

for div in soup.find_all('div', {'class': 'inner mobFront med colcMob'}):
    for mobCon in div.find_all('div', {'class': 'mobCon med'}):
        for id in mobCon.find_all('div'):
            contImg = id.find('div', {'class': 'contentImage'})
            if contImg:
                data.append(contImg.find('img')['data-original'])

time_input = input('How long between each meme? Enter in minutes: ')
try:
    time_input=int(time_input)*60
    while data:
        img_i = random.randint(0, len(data)-1)
        webbrowser.open_new_tab(data[img_i])
        del data[img_i]
        time.sleep(time_input)
except:
    print("Uh oh error this isn't good...")

