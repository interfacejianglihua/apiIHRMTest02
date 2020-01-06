# dict = {}
# print(dict)
# dict["k1"] = "v1"
# print(dict)
#
# dict["k2"] = "v2"
# print(dict)

# 1 导包
import pymysql
# 2 建立连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='books', port=3306,charset = "utf8")
# 3 获取游标
cursor = conn.cursor()
# 4 执行
# 查询图书表数据
select_sql = "select id, title, `read`, `comment` from t_book;"
cursor.execute(select_sql)
print("查询结果的总记录数为：", cursor.rowcount)
# 查询结果的第一条数据
print("查询结果的第一条数据为： {}".format(cursor.fetchone()))
# 获取全部的查询结果
# 注意：如果之前使用过fetchone或者fetchall，那么后续再使用fetchall时，会从上一个的指针位置读取数据
print("全部查询结果为：", cursor.fetchall())
# 要获取全部的查询结果，需要重新再执行查询语句
cursor.execute(select_sql)
# 再打印依次全部的结果
book_list = cursor.fetchall()
print("重新执行查询语句之后的结果为：", book_list)
# 打印每一本书
for book in book_list:
    print("书名为：", book[1])
# 5 关闭游标
cursor.close()
# 6 关闭连接
conn.close()