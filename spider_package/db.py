# coding:utf8
import traceback

import MySQLdb

def connect_db():

    db = MySQLdb.connect('localhost', 'root', 'jJ@123456', 'spider')

    cursor = db.cursor()

    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print 'Database version: %s ' % data

    return db, cursor



def insertData(data):
    db, cursor = connect_db()
    insert_data = data['data']
    sql = "INSERT INTO spider_data(data) \
            VALUES ('%s') " % (insert_data)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception, e:
        print traceback.print_exc()
        db.rollback()

    db.close()

if __name__ == '__main__':
	insertData({'data':'titlezhu'})


