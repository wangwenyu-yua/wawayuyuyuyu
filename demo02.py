"""
----------------判断-------------

"""

# 例子
# a=1
# b=2
# if a==1:
#     print("今天您好")
# if a>b:
#     print("a比b大")
# else:
#     print("b更大")

# age=int(input("请输入您的年龄"))
# if age>60:
#     print("您应该退休了")
# elif age>30:
#     print("家庭责任很重吧")
# elif age>20:
#     print("一定要好好规划未来")
# else:
#     print("读书的时候要认真")

# if age >20 and age<=30:
#     print("222222222")
# elif age>30:
#     print("333333")
# elif age>60:
#     print("666666")
# else:
#     print("78989225") 

    # # """
    # 判断条件           ==等于   
    #                   =  赋值
    #                 ！= 不等于
    #                 in：
    #                 is
    #                 not  in
    #                 not is
    #                 >
    #                 <
    
    # """
"""
a="您好"
if a in ("您好，今天吃了吗"):
    print("ok")
else:
    print("不ok")
     """

a = input("请输入")

if a=="":
    print("不能为空")
if a in"012456789":
    a=int(a)
else:
    print("请输入正确的年龄")
    exit()
if a > 5:
    print("大")
else:
    print("小")