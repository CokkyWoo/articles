from py_mysql import *
import pymysql
# 打开数据库连接
db = pymysql.connect('localhost', 'root', '', 'test002')
# db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test002')

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

mysql_client = MysqlClient()

# 使用预处理语句创建表
sql = '''CREATE TABLE `wechat` (
         `id` int(11) NOT NULL AUTO_INCREMENT,
         `wechat_id` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
         `wechat_name` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
         `headimage` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
         `introduction` varchar(500) NOT NULL DEFAULT '' ,
         `profile_url` varchar(500) CHARACTER SET utf8 NOT NULL DEFAULT '',
         `qrcode` varchar(500) CHARACTER SET utf8 NOT NULL DEFAULT '',
         `post_perm` int(11) NOT NULL DEFAULT '0',
          PRIMARY KEY (`id`))'''
mysql_client.query(sql)

# 关闭数据库连接
# db.close()
