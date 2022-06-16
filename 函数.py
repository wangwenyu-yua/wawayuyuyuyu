"""
函数方法  方法的定义：def  方法的名字  参数   方法的说明  方法的逻辑代码  return 返回数据

"""
"""
   自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
"""



# def checkname(username):
#     """
#    自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
# """
#     if len(username)>=5 and len(username) <= 8:
#         if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#             print("ok")
#         else:
#             print("账号必须以字母开头")
#     else:
#         print("您的账号不符合规则。请输入5-8位账号")

#def方法的声明
#checkname 方法的名字
#username 方法的参数
"""方法的说明""""""
   自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
"""
#方法的逻辑代码
# a="adhf7"
# checkname(a)
# """  加法方法  """
# def jiafa(a,b):
#     """这个方法作用是实现两个数字相加"""
#     if type(a) is int and type(b) is int:
#        return a+b
#     else:
#        return "输入类型不正确"
# # jiafa(3,88)
# # a=[]
# # print(a.append("哈哈"))#none
# # print(a.count("哈哈"))#1
# print(jiafa(1,1))

"""

返回值返回后 我们可以对这个其他的值做其他的操作 而print不能
"""


# a=[1,2,3,8,3,5,8,2]
# x=a.index(3)
# print(a[x])






def checkname(username):
    """
   自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
"""
    # if len(username)>=5 and len(username) <= 8:
    #     if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
    #        return True
    #     else:
    #         return "账号信息必须以小写字母开头"
  
    # return "您的账号不符合规则。请输入5-8位账号"

    
    username=input("请输入您的账号")
    password=input("请输入您的密码")
    if checkname(username)==True:
        if len(password) >= 8 and len(password) <=12:
            print("注册成功",{username:password})
        else:
        
            print("密码必须是8-12位")
    else:
            print(checkname(username))



"""
异常反馈
try:                  #try和except是搭配使用的
    print("a"+1)
except:
    print("上面的代码写错了")


try:                  #try和except是搭配使用的
    print("a"+1)
except Exception as a:
    print("上面的代码写错了",e)

"""

# 异常类  用来处理代码报错的
"""
包---类---方法---变量
并列的关系

"""