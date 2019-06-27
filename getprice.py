import bs4
import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("pair",help="The currency pair you wish to search",type=str)
args = parser.parse_args()

url = 'https://finance.yahoo.com/quote/{}%3DX?p={}%3DX'.format(args.pair,args.pair)
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text,"xml")
print(soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text)
