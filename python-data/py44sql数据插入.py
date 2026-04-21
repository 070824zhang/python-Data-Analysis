from pymysql import Connection

#构建到Mysql数据库链接
conn = Connection(
    host='localhost',      #主机名（IP）
    port=3306,             #端口
    user='root',            #账户
    password='147369',
    autocommit=True       #自动提交
)

cursor = conn.cursor()
conn.select_db("itcast")
cursor.execute("insert into student values(10004,'王力宏',21)")

#通过commit确认
#conn.commit()









