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

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"')
# chrome_options.add_argument('--headless')
headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
driver = webdriver.Chrome(options=options)

def parser():
	url = 'https://www.freeppt7.com/'
	url_3d = [
		'https://www.freeppt7.com/3D/list_12_1.html',
		'https://www.freeppt7.com/3D/list_12_2.html',
		'https://www.freeppt7.com/3D/list_12_3.html',
		'https://www.freeppt7.com/3D/list_12_4.html'

	]
	url_pink = ['https://www.freeppt7.com/pink/list_43_1.html',
				'https://www.freeppt7.com/pink/list_43_2.html'
				]

	url_animal = ['https://www.freeppt7.com/animal/']
	Chinese_wind = [
		'https://www.freeppt7.com/Chinese-wind/list_22_1.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_2.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_3.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_4.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_5.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_6.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_7.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_8.html',
		'https://www.freeppt7.com/Chinese-wind/list_22_9.html'
	]
	categories = {
		'1':'3D',
		'2':'Animal',
		'3':'Abstract'
	}
	categories = []
	wait = WebDriverWait(driver, 10)
	driver.get(Chinese_wind[2])
	driver.implicitly_wait(10)
	driver.refresh()
	# sleep(5)
	html_str = driver.page_source.encode('GBK', 'ignore')
	seletor = etree.HTML(html_str)
	categories_url = seletor.xpath('//*[@id="menu-primarynavigationmenu"]/li/ul/li/a/@href')
	categories = seletor.xpath('//*[@id="menu-primarynavigationmenu"]/li/ul/li/a/text()')

	# get all 'a' links to the list
	a_link = seletor.xpath('//*[@id="content"]/div/article/div/a/@href')
	# get all ppt titles to the list
	b_title = seletor.xpath('//*[@id="content"]/div/article/div/h2/a/b/text()')
	# get all images url to the list
	img_url = seletor.xpath('//*[@id="content"]/div/article/div/a/img/@src')
	# get all 'p' contents
	p_content = seletor.xpath('//*[@id="content"]/div/article/div/p/text()')

	# for i in range(len(a_link)):
	# 	print( b_title[i],'----->', a_link[i])
	# 	print(img_url[i])
	# 	# driver.get(img_url[i])
	# 	# sleep(5)
	# 	driver.get()

	return a_link, b_title, img_url, p_content
	driver.quit()
def get_data(a_link, b_title, img_url, p_content):
	headers = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
	}

	# print("****************", img_url, "****************")
	for i in range(len(img_url)):
		img_path = r'categories\Chinese_wind' + os.path.sep + b_title[i]
		if not os.path.exists(img_path):
			os.makedirs(img_path)

		options = webdriver.ChromeOptions()
		all_data_path = r'E:\Python\WorkSpace\PycharmProjects\freeppt\freeppt\categories\3D'+os.path.sep+b_title[i]
		# print("current ppt_path: %s" % all_data_path)

		# change chrome default save path
		prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': all_data_path}
		options.add_experimental_option('prefs', prefs)
		driver = webdriver.Chrome(options=options)

		imgname = img_url[i].split('/')[-1]
		img_name = imgname.split('.')[-2]+'.png'

		content_name = b_title[i]+'.txt'
		# print("current image name: %s " % img_name)
		img_obj = requests.get(img_url[i], headers=headers)
		sleep(1)

		content_obj = p_content[i]
		# print("current content_obj: %s" % content_obj)
		img_file_path = img_path + os.path.sep + img_name

		content_file_path = img_path + os.path.sep + content_name

		if not os.path.exists(img_file_path):
			with open(img_file_path, mode='wb') as f_img:
				f_img.write(img_obj.content)
			print('Downloaded image path is %s' % img_file_path)
		else:
			print('Already Downloaded', img_file_path)

		if not os.path.exists(content_file_path):
			with open(content_file_path, mode='w', encoding='utf-8') as f_content:
				f_content.write(str(content_obj))

			print('Downloaded content path is %s' % content_file_path)
		else:
			print('Already Downloaded', content_file_path)

		url_ppt = a_link[i]
		wait = WebDriverWait(driver, 10)
		driver.get(url_ppt)
		driver.implicitly_wait(10)
		driver.refresh()
		# sleep(5)
		html_str = driver.page_source.encode('GBK', 'ignore')
		seletor = etree.HTML(html_str)
		# get all ppt download href to the list
		ppt_download_href = seletor.xpath('//*[@id="content"]/article//strong/a/@href')[0]
		long_img_href = seletor.xpath('//*[@id="slider"]/div/img/@src')[0]
		# print("long_img_href:",long_img_href)
		# combine website and href into one link, just for downloading PPT
		ppt_download_url = 'https://www.freeppt7.com' + ppt_download_href
		long_img_url = 'https://www.freeppt7.com' + long_img_href
		# print("ppt download url: %s " % ppt_download_url)
		# print("long picture download url: %s " % long_img_url)

		# download long PPT preview picture
		img_name_long = 'long_preview_' + long_img_url.split('/')[-1]
		# print(img_name_long)
		# img_name_long_png = 'long_preview_' + img_name_long.split('.')[-2] + '.png'
		long_img_obj = requests.get(long_img_url, headers=headers)

		sleep(1)
		# save long PPT preview picture
		long_img_file_path = img_path + os.path.sep + img_name_long
		if not os.path.exists(long_img_file_path):
			with open(long_img_file_path, mode='wb') as f_img_long:
				f_img_long.write(long_img_obj.content)
			print('current: ',i,'/',len(img_url))
			print('Downloaded long PPT preview image path is %s' % long_img_file_path)

		else:
			print('Already Downloaded', long_img_file_path)
		sleep(3)
		ppt_name = ppt_download_url.split('/')[-1]
		# print(ppt_name, "is downloading...")
		ppt_obj = requests.get(ppt_download_url, headers=headers)
		sleep(1)
		# save long PPT preview picture
		ppt_file_path = img_path + os.path.sep + ppt_name
		if not os.path.exists(ppt_file_path):
			with open(ppt_file_path, mode='wb') as f_ppt:
				f_ppt.write(ppt_obj.content)
			print('Downloaded long PPT %s' % ppt_file_path)
		else:
			print('Already Downloaded', ppt_file_path)
		sleep(5)
		# driver.get(ppt_download_url)

def main():
	a_link = parser()[0]
	b_title = parser()[1]
	img_url = parser()[2]
	p_content = parser()[3]
	get_data(a_link, b_title, img_url, p_content)
if __name__ == '__main__':
	main()

