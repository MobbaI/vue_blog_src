# coding=utf-8
import pymysql
import json


host = 'localhost'
port = 3306
db = 'ios_data'
# user = 'mysql.infoschema'
user = 'root'
# password = '123456'
password = 'yzhnbznb'


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn


def get_data():

    conn = get_connection()

    # cursor = conn.cursor()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    with open('./static/data.json', encoding='utf-8') as f:
        ios_json = json.load(f)['iOS']

        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = "SELECT * FROM ios_data WHERE size = 10.2"

        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)

    conn.close()


if __name__ == '__main__':
    get_data()