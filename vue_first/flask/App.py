# coding=utf-8
from flask import Flask, request
from flask_cors import CORS
import json
import pymysql


app = Flask(__name__)
CORS(app, supports_credentials=True)

iOS_DATA = ''


def get_coon():
    conn = pymysql.connect(host='localhost', port=3306, db='ios_data', user='root', password='yzhnbznb')
    return conn


@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)


@app.route('/dataJson')
def get_json():

    conn = get_coon()

    # 默认为元组
    # cursor = conn.cursor()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM ios_data"

    cursor.execute(sql)

    iOS_DATA = json.dumps({"iOS": cursor.fetchall()})

    return iOS_DATA


@app.route('/dataSelect', methods=['POST', 'GET'])
# @app.route('/dataSelect')
def data_selet():
    options = {'': '', '001': 'p_name', '002': 'size', '003': 'resolution', '004': 'RAM', '005': 'CPU', '006': 'Model', '007': 'OpenGL_ES', '008': 'screen'}
    search_key = options[request.args.get('label')]
    search_temp = request.args.get('value')

    conn = get_coon()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if search_temp:
        sql = "SELECT * FROM ios_data WHERE {} REGEXP '{}'".format(search_key, search_temp)
    else:
        sql = "SELECT * FROM ios_data"

    cursor.execute(sql)

    iOS_DATA = json.dumps({"iOS": cursor.fetchall()})

    return iOS_DATA


if __name__ == '__main__':
    app.run(debug=True)