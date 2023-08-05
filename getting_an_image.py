import requests
import bs4

cherries = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

stew = bs4.BeautifulSoup(cherries.text,'lxml')

computer = stew.select('.mw-file-element')[4]

image_link2 = requests.get('https:'+computer['src'])

zulu = open('another_processor_image.jpg','wb')
zulu.write(image_link2.content)
zulu.close