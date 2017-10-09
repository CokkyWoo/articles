from py_mysql import *
import pymysql
# 打开数据库连接
db = pymysql.connect('localhost', 'root', '', 'test002')
mysql_client = MysqlClient()

# 使用预处理语句创建表
sql_wechat = '''CREATE TABLE `wechat` (
             `id` int(11) NOT NULL AUTO_INCREMENT,
             `wechat_id` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
             `name` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
             `descrption` varchar(500) NOT NULL DEFAULT '' ,
             `image_urls` varchar(500) CHARACTER SET utf8 NOT NULL DEFAULT '',
             `qrcode` varchar(500) CHARACTER SET utf8 NOT NULL DEFAULT '',
             `authentication` varchar(500) CHARACTER SET utf8 NOT NULL DEFAULT '',
             `post_perm` int(11) NOT NULL DEFAULT '0',
              PRIMARY KEY (`id`))'''

sql_articles = '''CREATE TABLE `article` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `wechat_id` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `wechat_name` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `send_id` int(11) NOT NULL DEFAULT '0' ,
            `msg_type` int(11) NOT NULL DEFAULT '49' ,
            `artcile_type` int(11) NOT NULL DEFAULT '0' ,
            `field_id` int(11) NOT NULL DEFAULT '0' ,
            `main` int(11) NOT NULL DEFAULT '0' ,
            `released_time` int(11) NOT NULL DEFAULT '0' ,
            `title` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `author` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `abstract` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `url` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `cover` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
            `content` LONGTEXT CHARACTER SET utf8 NULL ,
            `html` LONGTEXT CHARACTER SET utf8 NULL ,
            PRIMARY KEY (`id`))'''

mysql_client.query(sql_wechat)
mysql_client.query(sql_articles)
