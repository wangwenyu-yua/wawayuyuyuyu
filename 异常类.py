from logging import exception


# try和exception的使用
"""a=input("请输入您的名字")
b=input("请输入您的年龄")
if int(b)>18:
    print(a,"成年了")
else:
    print(a,"未成年")

"""

a=input("请输入您的名字")
b=input("请输入您的年龄")
try:
    if int(b)>18:
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄")

# 处理用户输入的数据