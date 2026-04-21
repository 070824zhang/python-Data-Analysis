from pymysql import Connection

#构建到Mysql数据库链接
conn = Connection(
    host='localhost',      #主机名（IP）
    port=3306,             #端口
    user='root',            #账户
    password='147369'
)
#print(conn.get_server_info())
#执行非查询性质sql
cursor = conn.cursor()    #获取到游标对象
#选择数据库
conn.select_db("itcast")
#执行sql
#cursor.execute("create table test_pymysql(id int)")
cursor.execute("select * from student")

results = cursor.fetchall()
print(results)
for r in results:
    print(r)
#关闭连接
conn.close()