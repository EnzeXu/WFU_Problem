import pymysql
import pymysql.cursors

MYSQL_PARAMS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "enze",
    "passwd": "123456",
    "db": "wfu_problem"
}

class MySQLConnection:
    def __init__(self, params=MYSQL_PARAMS):
        self.connection_params = params
        self.connection = pymysql.connect(**self.connection_params)
        self.cursor: pymysql.cursors.Cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def executemany(self, command, tuples):
        self.cursor.executemany(command, tuples)
        return self.cursor.fetchall()


if __name__ == "__main__":
    mysql = MySQLConnection()
    # mysql.execute("insert into test.t1 values (3, 'ball', 20);")
    res = mysql.execute("select * from wfu_problem.`user`;")
    # res = mysql.execute("select * from test.t1;")
    print(res)


