# coding:utf8
import url_manage, html_download, html_parser, html_output
import traceback
import re


class SpiderMain(object):

	def __init__(self, options):
		self.options = options
	
		self.urls = url_manage.UrlManage()
		self.download = html_download.HtmlDownload()
		self.parser = html_parser.HtmlParser(options['urlReg'], options['urlData'])
		self.output = html_output.HtmlOutput()


	def craw(self):
		if root_url is None:
			print 'root_url is None'
			return

		self.urls.add_new_url(self.options['root_url'])

		count = 1;
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()

				print 'craw %d: %s' % (count, new_url)

				html_str = self.download.download(new_url)

				# print html_str

				new_urls, new_data = self.parser.parser(new_url, html_str)

				self.urls.add_new_urls(new_urls)
				self.output.collect_data(new_data)

			except Exception, e:
				print 'craw failed '
				traceback.print_exc()


			if count == self.options['max_count']:
				break
			count = count + 1

		self.output.html_output()


if __name__ == '__main__':
	print '请输入入口url:'
	root_url = raw_input('入口url：')

	print '====================================='
	max_count = 1
	while True:
		print '请输入最大收集条数，大于1的正整数, 0默认收集10条'
		max_count = int(input('最大收集条数:'))
		if max_count > 1 or  max_count == 0:
			if max_count == 0:
				max_count = 10
			break

	print '\n'
	print '================================='
	print '请输入需要收集的url格式'
	print '1. 完整url格式, 默认模式'
	print '2. 域名+部分url格式'

	urlType = int(input('请选择url格式：'))

	urlStr = ''
	urlRe = r'^http(s?)://(\w+.+)\w' 
	if urlType == 2:
		# while True:
		# 	url1 = raw_input('请输入带完整域名的url1:')
		# 	urlTest = re.match(urlRe, url1)

		# 	if not (urlTest) is None:
		# 		break

		urlStr = raw_input('请输入urlStr:')

	else :
		while True:
			urlStr = raw_input('请输入带完整域名的urlStr:')
			urlTest = re.match(urlRe, urlStr)

			if not (urlTest) is None:
				break
	
	urlReTest = {'urlRegType': urlType, 'urlReg': urlStr}

	options = {}
	options['root_url'] = root_url
	options['max_count'] = max_count
	options['urlReg'] = urlReTest
	options['urlData'] = []

	sp = SpiderMain(options)
	sp.craw()
