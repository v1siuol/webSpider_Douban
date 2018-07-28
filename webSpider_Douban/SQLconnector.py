import mysql.connector
from mysql.connector import errorcode

class SQLconnector:
    def __init__(self):
        pass

    def initial(self):

        config = {
            "user": "root",
            "password": "root",
            "host": "127.0.0.1",
            'raise_on_warnings': True
        }

        # 连接本地服务器
        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print('haha')
                print(err)

        cursor = cnx.cursor()
        DB_NAME = "webSpider_Douban"

        # cursor.executF NOT EXISTS webSpider_Douban")

        # 数据库
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                pass
            else:
                print(err)
        # cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))
        cursor.execute("USE {};".format(DB_NAME))

        # 表格 if no exists doesn't work idk
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                pass
            else:
                print(err)

        # 插入
        # try:
        #     # INSERT INTO movies (name) VALUES ('测试');
        #     sql = "INSERT INTO movies (name) VALUES (%s)"
        #     val = ('测试',)
        #     ret = cursor.execute(sql, val)
        # except mysql.connector.Error as err:
        #     print(err)

        cnx.commit()

        # 查询
        # cursor.execute("SELECT * FROM movies");
        # values = cursor.fetchall()
        # print(values)

        
        print('ok')
        cursor.close()
        cnx.close()

def test():
    a = SQLconnector()
    a.initial()

test()