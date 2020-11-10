import scrapy
import urllib
import requests
import re
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import json

class DmozItem(scrapy.Item):
	Location = scrapy.Field()
	Title = scrapy.Field()

class DmozSpider(scrapy.Spider):
	name = "dicee"
	page_numbers = 120
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		"origin": "https://www.dice.com",
		"referer": "https://www.dice.com/",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
		"x-api-key": "1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8"
	}
	start_urls = [
	'https://www.ziprecruiter.com/candidate/search?radius=25&search=&location=Minneapolis%2C+MN+USA'
	]
	def parse(self,response):
		url = 'https://www.ziprecruiter.com/candidate/search?radius=25&search=&location=Minneapolis%2C+MN+USA'
		request = scrapy.Request(url,callback=self.parse_api,headers=self.headers)
		yield request

	def parse_api(self,response):
		urls = response.url
		print(urls)