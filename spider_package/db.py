# coding:utf8
import traceback

import MySQLdb
import redis_config

redisCs = redis_config.CRedis()

def connect_db():

# db = MySQLdb.connect('localhost', 'root', 'jJ@123456', 'spider')
    db = MySQLdb.connect('localhost', 'root', '123456', 'spider')

    cursor = db.cursor()

    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print 'Database version: %s ' % data

    return db, cursor



def insertData(data):
    db, cursor = connect_db()
    oldData = redisCs.getData('spider_list_old')

    for item in data:
        insert_data = item
        sql = "INSERT INTO spider_data(data) \
                VALUES ('%s') " % (insert_data)

        try:
            if item not in oldData:
                cursor.execute(sql)
                db.commit()
            redisCs.delData(item)
            redisCs.setData('spider_list_old', item)

        except Exception, e:
            print traceback.print_exc()
            db.rollback()

    db.close()

if __name__ == '__main__':
    datas = redisCs.getData('spider_list')
    insertData(datas)


