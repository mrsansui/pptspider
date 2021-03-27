# -*- coding: utf-8 -*-
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
from lxml.html import fromstring, tostring
from bs4 import BeautifulSoup
import os

# options = webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"')
# options.add_argument('--headless')
headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
# driver = webdriver.Chrome(options=options)

def parser():
    url = 'https://www.freeppt7.com/Chinese-wind/list_22_3.html'
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content.decode(errors="ignore"), 'lxml')
    html_path = "freeppt.html"
    # with open(html_path, 'wb') as f:
    #     f.write(bs.text)

    # print(soup)
    print(soup.select('li>a>href'))
    # print(soup.select(".post-thumb"))


if __name__ == "__main__":
    parser()