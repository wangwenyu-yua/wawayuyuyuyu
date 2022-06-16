"""
1.包：  系统自带的包 利用import导入 第三方的包
2.模块
3.类


"""

# 1.系统自带的包
"""
from os import curdir
import time
import random  #生成随机数
a=random.randint(10,100)
for i in range(10):
    time.sleep(1)#控制运行速度  每隔一秒运行一下
    print(i)
    print(a)
"""
""" 2.第三方的包  pip工具管理  第三包的工具  1.pip install 包名 安装包  2.pip  uninsatll 包名 卸载第三方包3.pip list  查看安装的包
常用的第三方包   第三方的包在py中的 scripts中的文件夹之中
1.操作mysql数据库的包  pymysql     
2.web自动化   selenium
3.app自动化的包  appium
4.接口自动化的包  requests
5.操作excel表的包  xlrd
6.写入eccel的包   xlwt


"""
# 2.第三方包的使用   例子pymysql

import pymysql
db=pymysql.connect (host="127.0.0.1",user="root",passwd="root",db="shop")
cur=db.cursor()
try:
    cur.execute("select * from sc;")
    res=cur.fetchall()
except:
    print(res)
