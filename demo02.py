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

# a = input("请输入")

# if a=="":
#     print("不能为空")
# if a in"012456789":
#     a=int(a)
# else:
#     print("请输入正确的年龄")
#     exit()#退出的意思
# if a > 5:
#     print("大")
# else:
#     print("小")



# is的用法:判断输入的类型  
# a=10
# if type(a) is int:
#     print("是数字")
# if type(a) is str:
#     print("是字符串")
# else:
#     print("其他")


# if

# if else            三种判断类型

# if elif else

"""

循环类型：while   for

"""



# from turtle import update
# from unicodedata import name


# a=1  
# while a<10:
#     print("太小了")
#     a=a+1


"""
    练习：现在有10个学生成绩  需要录入到系统中。这十个人分别是  王1 王2 王3 王4 王5 王6 王7  王8   王9   压索
    并且名字和成绩对应上  而且大于60的  和小于60的  需要分开存放 


    分析：字典存放姓名和成绩使之分开存放   
    数组 字典可以将成绩划分
    录入用input处理


    
    """
# a=[]
# b=[]
# name=input("请输入学生的姓名")
# socre=input("请输入学生的成绩")
# if socre<60:
#     print(a)
# if socre>60:
#     print(b)
# zon={}
# zon=update(name=socre)

high={}
low={}
studentlist=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
a=0
while a<len(studentlist):
   chengji= int(input("请输入"+studentlist[a]+"成绩"))
   if chengji>=60:
        high[studentlist[a]]=chengji
   else:
        low[studentlist[a]]=chengji
   a=a+1
print(high,"成绩还不错的")
print(low,"成绩不太行")
   












    