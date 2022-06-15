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

# high={}#定义一个空字典来存储大于60的信息

# low={}#定义一个空字典 用来存储小于60的信息
# studentlist=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
# a=0#定义一个变量来用来控制数组的下标变化
# while a<len(studentlist):#因为所以的人信息的录入，都要用input 所以写了循环，len判断了数组长度 总长度-1就是最大的下标
#    chengji= int(input("请输入"+studentlist[a]+"成绩"))#获取这个录入信息 并且为了方便判断转换了格式 字符串的拼接
#    if chengji>=60:#判断分数
#         high[studentlist[a]]=chengji#存到字典中
#    else:
#         low[studentlist[a]]=chengji
#    a=a+1#用来控制下标变化的，每一次循环都增1
# print(high,"成绩还不错的")
# print(low,"成绩不太行")
   


#6.15
"""
for循环:通过遍历来实现的
range()方法

"""
# a="您好  今天您学习了吗"
# for i in a:
#     print(i)


# b=list(range(0,100,2))#自动生成了一个数列   list代表数组  步进/步长
# print(i)

# for i in range(10):
#     print(i)


# high={}#定义一个空字典来存储大于60的信息

# low={}#定义一个空字典 用来存储小于60的信息
# studentlist=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
# a=0#定义一个变量来用来控制数组的下标变化
# while a<len(studentlist):#因为所以的人信息的录入，都要用input 所以写了循环，len判断了数组长度 总长度-1就是最大的下标
#    chengji= int(input("请输入"+studentlist[a]+"成绩"))#获取这个录入信息 并且为了方便判断转换了格式 字符串的拼接
#    if chengji>=60:#判断分数
#         high[studentlist[a]]=chengji#存到字典中
#    else:
#         low[studentlist[a]]=chengji
#    a=a+1#用来控制下标变化的，每一次循环都增1
# print(high,"成绩还不错的")
# print(low,"成绩不太行")
   


#练习:打印九九乘法表


# for j  in range(1,10):
#     for i in range(1,j+1):
#         print(i,"x",j,"=",i*j,end=" ")#end不会换行 
#     print()


for red in range(0,31):
    for red in range(red,red+1):
        if red==30:
            print("红灯结束啦")
        else:
            print(red+1,end="...")
for green in range(1,36):
    for green in range(green,green+1):
        if green==35:
            print("绿灯结束了 请等待")
        else:
            print(green+1,end="...")
for yellow in range(0,4):
    for yellow in range(yellow,yellow+1):
        if yellow==3:
            print("黄灯结束！！！")
        else:
            print(yellow+1,end="...")




#end示例
# a=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
# for i in a:
#     print(i,end="||")    
#     print("---------------------------")







    