import datetime
import os
import re

import requests
from bs4 import BeautifulSoup

today = datetime.datetime.now()
curr_date = f'{today.strftime("%B")} {today.day}, {today.year}'
print(curr_date)

html = requests.get('https://ptv.org/radio/').text
soup = BeautifulSoup(html, 'html.parser')

last_broadcast_date = soup.find('span', {"class": "post-audio-date"}).text

if curr_date == last_broadcast_date:
    brdcst = soup.find(lambda tag: tag.name == 'a' and tag.get('class') == ['popup-launch'])
    pdcst_name = brdcst.text
    series_name = soup.find('h3', {'class': 'broadcast-title'}).text
    pdcst_desc = soup.find('div', {'class': 'post-audio-discription'}).text

    pdcst_addr1 = brdcst.get('href')
    pdcst_href1 = requests.get(pdcst_addr1).text
    pdcst_soup1 = BeautifulSoup(pdcst_href1, 'html.parser')
    
    pdcst_addr2 = pdcst_soup1.find('iframe').get('src')
    pdcst_href2 = requests.get(pdcst_addr2).text
    pdcst_soup2 = BeautifulSoup(pdcst_href2, 'html.parser')

    audio_file_url = pdcst_soup2.find('source').get('src')
    audio_file = requests.get(audio_file_url)

    desc_filename = f'./{series_name}/{pdcst_name}.txt'
    os.makedirs(os.path.dirname(desc_filename), exist_ok=True)
    
    audio_filename = f'./{series_name}/{pdcst_name}.mp3'
    os.makedirs(os.path.dirname(audio_filename), exist_ok=True)
    
    with open(audio_filename, 'wb') as af: 
        af.write(audio_file.content)

    with open(desc_filename, 'w') as df:
        df.write(pdcst_desc)

else:
    break