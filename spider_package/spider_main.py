# coding:utf8
import url_manage, html_download, html_parser, html_output
import traceback
import re
import redis_config

import config
import db

class SpiderMain(object):

    def __init__(self, options):
        self.options = options
        print options
    
        self.urls = url_manage.UrlManage()
        self.download = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser(options['urlReg'], options['urlData'])
        self.output = html_output.HtmlOutput()
        self.redis = redis_config.CRedis()


    def craw(self):
        if self.options['root_url'] is None:
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
#db.insertData(new_data)
                
                self.redis.setData('spider_list', new_data)

            except Exception, e:
                print 'craw failed '
                traceback.print_exc()


            if count == self.options['max_count']:
                break
            count = count + 1

        self.output.html_output()


if __name__ == '__main__':
    options = config.initOptions()

    sp = SpiderMain(options)
    sp.craw()
