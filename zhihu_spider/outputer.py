#coding:utf-8
import MySQLdb

class Outputer(object):

    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='zhihu', charset='utf8')
        self.cursor = self.conn.cursor()

    # 存储用户数据
    def save(self, base_data):
        try:
            sql = "insert into user_(id,nickname,sex,living_place,field,job,education,picture_url,interest,signature,question,fans,answers,followees,topics,zan,thanks) " \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            param = (base_data["id"], base_data["nickname"], base_data["sex"], base_data["living_place"],
                 base_data["field"], base_data["job"], base_data["education"], base_data["picture_url"],
                 base_data["interest"], base_data["signature"], base_data["question"], base_data["fans"],
                 base_data["answers"],base_data["followees"],base_data["topics"], base_data["zan"], base_data["thanks"])

            self.cursor.execute(sql, param)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()

    # 查询数据库判断此链接是否访问过
    def isCrawed(self, url):
        try:
            sql = "select * from old_url where url=%s"
            param = (url)

            self.cursor.execute(sql, param)
            re = self.cursor.fetchall()
            self.conn.commit()
            if len(re) != 0:
                return True
            else:
                return False
        except Exception as e:
            print e
            self.conn.rollback()

    def add_old_url(self, url):
        try:
            sql = "insert into old_url(url) values(%s)"
            param = (url)
            self.cursor.execute(sql, param)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()

    def isSaved(self, url):
        try:
            sql = "select * from new_url where url=%s"
            param = (url)

            self.cursor.execute(sql, param)
            re = self.cursor.fetchall()
            self.conn.commit()
            if len(re) != 0:
                return True
            else:
                return False
        except Exception as e:
            print e
            self.conn.rollback()

    def has_new_url(self):
        try:
            sql = "select * from new_url "

            self.cursor.execute(sql)
            re = self.cursor.fetchall()
            self.conn.commit()
            if len(re) != 0:
                return True
            else:
                return False
        except Exception as e:
            print e
            self.conn.rollback()

    def add_new_url(self, url):
        try:
            sql = "insert into new_url(url) values(%s)"
            param = (url)
            self.cursor.execute(sql, param)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()

    def pop_new_url(self):
        try:
            sql = "select * from new_url"
            sql2 = "delete from new_url where url=%s"
            self.cursor.execute(sql)
            self.conn.commit()
            re = self.cursor.fetchone()
            new_url = str(re[0])
            param = (new_url)
            self.cursor.execute(sql2, param)
            self.conn.commit()
            self.add_old_url(new_url)
            return new_url
        except Exception as e:
            print e
            self.conn.rollback()


    def close(self):
        self.cursor.close()
        self.conn.close()

