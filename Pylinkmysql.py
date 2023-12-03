import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
#  user="pythonpractiseadmin",    # 数据库用户名
  user="root",    # 数据库用户名
  passwd="xxxxxxxx",   # 数据库密码
  auth_plugin="mysql_native_password"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("select * from mysql.user;")

for x in mycursor:
  print(x)