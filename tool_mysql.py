'''
mysql 导出入小工具

'''

import pymysql

class Mysql:
    def __init__(self, host, password, user, database, port, charset, file_adress, table):
        self.host=host#地址
        self.password=password#密码
        self.user=user#用户名
        self.database=database#库名称
        self.port=port#端口
        self.charset=charset#编码格式
        self.file_adress=file_adress#导入文件地址以及名称
        self.table=table #表名称


    #导入数据库
    def mysql_input(self):
        #链接数据库
        db=pymysql.connect(host=self.host,
                           password=self.password,
                           user=self.user,
                           database=self.database,
                           port=self.port,
                           charset=self.charset)
        #创建游标
        cur=db.cursor()
        #导入数据的sql语句
        sql="load data infile '%s' " \
            "into table %s " \
            "fields terminated by ','" \
            "lines terminated by '\n';"%(self.file_adress,self.table)

        try:
            #执行sql命令
            cur.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            #出错执行回滚
            db.rollback()
        # 关闭游标
        cur.close()

        # 关闭数据库
        db.close()

    #导出csv文件
    def mysql_output(self):
        # 链接数据库
        db = pymysql.connect(host=self.host,
                           password=self.password,
                           user=self.user,
                           database=self.database,
                           port=self.port,
                           charset=self.charset)

        # 创建游标
        cur = db.cursor()
        # 导入数据的sql语句
        sql = "select * from %s " \
              "into outfile '%s' " \
              "fields terminated by ',' " \
              "lines terminated by '\n';"%(self.table,self.file_adress)

        try:
            # 执行sql命令
            cur.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            # 出错执行回滚
            db.rollback()

if __name__ == '__main__':
    #创建实例对象
    sql=Mysql(host='localhost',
                    port = 3306,
                    user='root',
                    password = '123456',
                    database = 'db2',
                    charset='utf8',
                    #linux 一般导入导出的安全目录为/var/lib/mysql-files
                    file_adress='/var/lib/mysql-files/test_score.csv',
                    table='scoretab'
              )
    #调用导出方法
    sql.mysql_output()
    #调用导入方法
    # sql.mysql_input()


