import pymysql
import pymysql.cursors

from const import DB_HOST

MYSQL_PARAMS = {
    "host": DB_HOST,
    "port": 3306,
    "user": "wfu",
    "passwd": "123456",
    "db": "wfu_problem"
}


class MySQLConnection:
    def __init__(self, params=None):
        self.connection_params = MYSQL_PARAMS if params is None else params
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
    test_params = {
        "host": "127.0.0.1", #"18.117.181.47",
        "port": 3306,
        "user": "wfu",
        "passwd": "123456",
        "db": "wfu_problem"
    }
    mysql = MySQLConnection(test_params)
    # mysql.execute("insert into test.t1 values (3, 'ball', 20);")
    res = mysql.execute("select * from wfu_problem.`user`;")
    # res = mysql.execute("select * from test.t1;")
    print(res)


