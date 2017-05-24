# coding:utf8
import traceback

import MySQLdb

def connect_db():

    db = MySQLdb.connect('localhost', 'root', '123456', 'jia')

    cursor = db.cursor()

    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print 'Database version: %s ' % data

    return db, cursor



def insertData(data):
    db, cursor = connect_db()
    url = data['url']
    title = data['title']
    sql = "INSERT INTO spider_test(url, title) \
            VALUES ('%s', '%s') " % (url, title)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception, e:
        print traceback.print_exc()
        db.rollback()

    db.close()

if __name__ == '__main__':
    insertData({'url':'www', 'title': 'zhu'})


