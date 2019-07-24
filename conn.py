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
        try:
            conn = psycopg2.connect(database=app.config['DBNAME'], user=app.config['DBUSER'], password=app.config['DBPASSWORD'], host=app.config['DBURL'], port=app.config['DBPORT'])
            cursor = conn.cursor()
            cursor.execute(self.sql)
            conn.commit()
            return cursor.fetchall()
        finally:
            self.pgClose(conn)

    def pgClose(self, conn):
        """
        断开数据库链接
        :param conn:
        :return:
        """
        conn.close()
