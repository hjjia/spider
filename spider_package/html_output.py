# coding:utf8

class HtmlOutput(object):

	def __init__(self):
		self.datas = []
	
	def collect_data(self, data):
		self.datas.append(data)


	def html_output(self):
		fl = open('output.html', 'w')

		fl.write('<!DOCTYPE html>')
		fl.write('<html>')
		fl.write('<body>')
		fl.write('<table>')

		for data in self.datas:
			fl.write('<tr>')
			fl.write('<td>%s</td>' % data['url'].encode('utf-8'))
			fl.write('<td>%s</td>' % data['title'].encode('utf-8'))
			fl.write('</tr>')

		fl.write('</table>')
		fl.write('</body>')
		fl.write('</html>')

		fl.close()
