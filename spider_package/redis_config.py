# coding:utf8

import redis
import traceback
import json


class CRedis:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379
        self.db = 0
        self.r = redis.Redis(host = self.host, port = self.port, db = self.db)

    def setData(self, setName, data):
        convert_data = json.dumps(data)
        try:
            self.r.sadd(setName, convert_data)
        except Exception,e:
            print 'add failed'
            print traceback.print_exc()


    def getData(self, key):
        data = self.r.smembers(key)
        return data

    def delData(self, data):	

        self.r.srem('spider_list', data)


if __name__ == '__main__':
    cs = CRedis()
    cs.setData('spider_list', 'ddd')
