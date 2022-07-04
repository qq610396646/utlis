import time

import pymysql


class Connection_pymysql(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8")
        self.cursor = self.conn.cursor()

    def close_cursor(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        counter = self.cursor.execute(sql)
        return self.cursor, counter