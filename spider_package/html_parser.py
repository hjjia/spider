# coding:utf8

import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

	def __init__(self, urlReg, urlData):
		self.urlReg = urlReg
		self.urlData = urlData

	def _get_new_urls(self, url, soup):
		new_urls = set()

		links = soup.find_all('a', href=re.compile(self.urlReg['urlReg']))

		for link in links:
			new_url = link['href']
			full_url = ''

			if self.urlReg['urlRegType'] == 2:
				full_url = urlparse.urljoin(url, new_url)
			else:
				full_url = new_url
				
			new_urls.add(full_url)

		return new_urls


	def _get_new_data(self, url, soup):
		new_data = {}

		new_data['url'] = url

		# title_node = soup.find('div', class_='dRow').find('h2', class_='title show-title')
	#	new_data['title'] = title_node.get_text()
		new_data['title'] = ''


		return new_data


	def parser(self, url, html_str):
		if url is None or html_str is None:
			return None

		soup = BeautifulSoup(html_str, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(url, soup)
		new_data = self._get_new_data(url, soup)

		return new_urls, new_data


