# # 1.1
# #数据格式的转换

# #a=input()
# #b=input()
# #print("input获取的内容",a+b)

# # print(type("哈哈"))
# # print(type(23333))
# # print(type(2.333))
# # print(type(True))
# # print(type(()))
# # print(type([]))
# # print(type({}))

# # a=str(2333)
# # print(type(a))


# # 字符串/str
# # 整数/int
# # 小数/float
# # 布尔值/bool  True or  False
# # 元组/tuple
# # 数组/list
# # 字典/dict
# # 空 /NoneType   None




# # 2:任何数据都可以转换为字符串
# # 整数和小数可以互相转换
# # 字符串转换为其他的数据必须满足长得像这个规律

# # a=float (input("请输入"))
# # b=float (input("请输入"))
# # print("input获取的内容",a+b)


# # a='fhedojkpfjirhejkowdplokfjik   kjndoj'
# # print(len(a))


# '''
# 通过代码获取不同的两段内容并且计算他们长度的和


# '''
# # a='fhedojkpfjirhejkowdplokfjik   kjndoj'
# # b='fhsjjfsdkhfsdjk'
# # print(len(a+b))


# # a=input("请输入")
# # b=input("请输入")
# # print("两段字符的长度是：",len(a)+len(b))


# # 元组/tuple    下标从零开始编号  

# # a=() #空的元组
# # a=(1,2,3,"哈哈",True,False)

# # print(a[5])

# # a=(1,2,"nihao","True","哈哈哈哈哈","nihao")
# # # print(a[4],a[3])
# # print (a.index("nihao"))
# # print(a.index("哈哈哈哈哈"))

# # print(a.count("nihao"))





# # 元组说明：index():查找某个值的下标   count():统计某个值的数量


# # 二维元组





# # from this import d


# # a=(1,2,"nihao","True","哈哈哈哈哈","nihao")
# # c=(1.2,2,8,9,"d",8)
# # b=(a,c,"嘻嘻")

# # print(b[0][3])
# # print(b[1][4])

# # 切片
# # a=(1,2,3,"哈哈",True,False)
# # print(a[-1])
# # print(a[-4])
# # print(a[0:4])    #左闭右开
# # print(a[4:])

# #数组     数组与元组的区别 元组写好后不能修改  数组是可以修改的



# # a=[1,2,"nihao","True","哈哈哈哈哈","nihao"]
# # a.append("王文宇") #增加王文宇到数组之中   append是追加数据到数组之中的 只会往最尾端增加 固定的只能放在末尾
# # a.append("wawayu")
# # a.insert(0,"jake")#insert 可以插数据到任意位置 往数组中指定的位置插入数据
# # print(a)
# # a.pop(1)
# # print(a)

# # a=[1,2,"nihao","True","哈哈哈哈哈","nihao"]
# # a.insert(4,"添加")
# # b=a.pop(0)#剪切
# # print(b)#输出
# # c=a.pop(0)#剪切
# # print(c)#输出
# # print(b+c)#剪切相加
# # print(a)#输出剪切后的结果

# # # pop总结：剪切移动数据 从数组中剪切数据
# # # 
# # b=["nin","day1"]

# # print(a+b)

# # #extend()总结：合并数组
# # #clear() 总结：清空数组中的数据
# # #remove()总结：删除某个值
# # a.remove("添加")
# # xx=a.remove(1)
# # print(b)
# # print(a)
# #下标不要超出范围=越界
# # xx=[a,0,1,2,3]
# """
# 所以的小方法都是小括号结尾的 比如 print()extend()len()
# 元组，数组，字典、的取值都是用中括号比如 a[]
# 元组、数组、字典、的定分别是()[]{}
# """



# #字典/dict
# """
# 用{}来定义的  字典的特点：1：字典中的值没有顺序
# 2：字典的结构必须是键值对的结构   key:value 例如 a={"name":"张三"}  key=name  value=张三
# 3：字典的取值是通过key去取这个value  任何地方的字符串都要加引号

# """



# # from unicodedata import name


# # a={"name":"张三",0:"haha","age":25} 
# # """取值"""
# # print(a["name"])
# # """新增"""
# # a["high"]="183cm"
# # print(a)
# # """修改"""
# # a["name"]="李四"
# # print(a)


# # """
# # get:取值
# # pop:剪切
# # update:更新 新增或者修改
# # """
# # b=a.get("name")
# # print(b)
# # b=a.pop("name")
# # print(a)
# # a.update(name=1111)#这里name没有加引号 相当于定义一个name的变量  不需要加引号  
# # print(a)


# # """通用删除的方法    数组与字典     """

# # del a["name"]
# # print(a)

# # del a[0]


# # """练习  获取用户输入的个人信息 并且存储到字典中
# # 个人信息包括 name  age  sex
# # """
# name=input("请输入您的姓名")
# age=input("请输入您的年龄")
# sex=input("请输入您的性别")
# userinfo={}
# userinfo.update(name=name,sex=sex,age=age)
# print(userinfo)


# # 元组 
# # 数组 列表   list
# # 字典

# """判断"""


