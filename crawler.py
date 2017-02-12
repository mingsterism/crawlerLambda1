from bs4 import BeautifulSoup
import requests
from lxml import html
from collections import deque
import argparse

def handler(event, content):
	# parser = argparse.ArgumentParser()
	# parser.add_argument("--url", type=str)
	# args = parser.parse_args()
	# url = args.url.strip()
	r = requests.get(event['url'])
	print(r.content)
	return r.content
