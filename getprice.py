import bs4
import requests
import argparse
from bs4 import BeautifulSoup

def Main():
	#parse arguments for cli
	parser = argparse.ArgumentParser()
	parser.add_argument("pair",help="The currency pair you wish to search",type=str)
	parser.add_argument("-a", default=1, metavar=("amount"), help="The amount you wish to transfer (defaults to 1)",type=float)
	args = parser.parse_args()
	print(getprice(args.pair, args.a))

def getprice(currency, amount):
	#send get request to yahoo
	url = 'https://finance.yahoo.com/quote/{}%3DX?p={}%3DX'.format(currency,currency)
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text,"xml")
	try:
		#find currency element from xml
		price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
	except IndexError:
		return
	return float(price) * amount

if(__name__ == "__main__"):
	Main()
