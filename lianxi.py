"""练习：现在有10个学生成绩  需要录入到系统中。这十个人分别是  王1 王2 王3 王4 王5 王6 王7  王8   王9   压索
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

high={}#定义一个空字典来存储大于60的信息

low={}#定义一个空字典 用来存储小于60的信息
studentlist=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
a=0#定义一个变量来用来控制数组的下标变化
while a<len(studentlist):#因为所以的人信息的录入，都要用input 所以写了循环，len判断了数组长度 总长度-1就是最大的下标
   chengji= int(input("请输入"+studentlist[a]+"成绩"))#获取这个录入信息 并且为了方便判断转换了格式 字符串的拼接
   if chengji>=60:#判断分数
        high[studentlist[a]]=chengji#存到字典中
   else:
        low[studentlist[a]]=chengji
   a=a+1#用来控制下标变化的，每一次循环都增1
print(high,"成绩还不错的")
print(low,"成绩不太行")
   


   # """练习  获取用户输入的个人信息 并且存储到字典中
# 个人信息包括 name  age  sex
# """
name=input("请输入您的姓名")
age=input("请输入您的年龄")
sex=input("请输入您的性别")
userinfo={}
userinfo.update(name=name,sex=sex,age=age)
print(userinfo)



high={}#定义一个空字典来存储大于60的信息

low={}#定义一个空字典 用来存储小于60的信息
studentlist=["王1", "王2","王3","王4", "王5","王6","王7", "王8","王9", "压缩",]
for i in studentlist:
#因为所以的人信息的录入，都要用input 所以写了循环，len判断了数组长度 总长度-1就是最大的下标
   chengji= int(input("请输入"+i+"成绩"))#获取这个录入信息 并且为了方便判断转换了格式 字符串的拼接
   if chengji>=60:#判断分数
        high[i]=chengji#存到字典中
   else:
        low[i]=chengji
   a=a+1#用来控制下标变化的，每一次循环都增1
print(high,"成绩还不错的")
print(low,"成绩不太行")


"""
练习1：通过print实习一个红绿灯的功能  红灯30次  绿灯35次  黄灯3次
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




light={"红灯":35,"绿灯":30,"黄灯":5}
while True:
    for i in light:
        for j in range(light[i]):
            print(i,j)

练习2：使用代码实习一个注册的功能。用户输入账号和密码  要求账号长度是5-8位  密码6-12位并且账号必须小写字母开头无限制
储存在字典中
username=input("请输入您的账号")
password=("请输入您的密码")
if len(username)>=5 and len(username) <= 8:
    if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
        if len(password) >= 8 and len(password) <=12:
            print("注册成功",{username:password})
        else:
            print("密码必须是8-12位")
    else:
        print("账号必须以字母开头")
else:
    print("您的账号不符合规则。请输入5-8位账号")


"""

"""
定义：定义一个方法来判断用户输入的账号和密码是否符合标准
自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
"""
def  checkname(username,password):
# """
#    自动判断  账号长度是5-8位  密码6-12位并且账号必须小写字母
# """
    if len(username)>=5 and len(username) <= 8:
        if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
            if len(password)>=6 and len(password)<=12:
                return True
            else:
                return"密码不符合规范"
        else:
            return "账号信息必须以小写字母开头"
  
    return "您的账号不符合规则。请输入5-8位账号"