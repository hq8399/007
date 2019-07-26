# -*- coding: utf-8 -*-

from flask import Flask
import psycopg2

app = Flask(__name__)
app.config.from_object('config')


class DbConn:
    def __init__(self, sql):
        self.sql = sql

    def pgConn(self):
        """
        链接数据库,执行SQL
        :param sql:
        :return:
        """
        conn = psycopg2.connect(database=app.config['DBNAME'], user=app.config['DBUSER'], password=app.config['DBPASSWORD'], host=app.config['DBURL'], port=app.config['DBPORT'])
        cursor = conn.cursor()
        try:
            cursor.execute(self.sql)
            coloumns = [row[0] for row in cursor.description]
            result = [[str(item) for item in row] for row in cursor.fetchall()]
            return [dict(zip(coloumns, row)) for row in result]
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
