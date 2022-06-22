"""
常见数据类型分类
将生活中常见的数据类型划分为不同的类型 因为不同的类型可以进行的操作是不一样的
数字需要加减乘除  而文字却不需要
1.数字类型
    整型  int  就是整数 既不带小数点的数
    浮点型 float  就是小数
    布尔类型  bool  只有两个值 真TRUE  假 FALSE     注意 非0即真
        TRUE   1 和  FALSE  0 都是关键字 注意大小写
2.复数类型 3+4i，
    字符串：----str---使用引号引起来的就是字符串
    列表   list  【1，2，3】
    元组   tuple （1，2，3）
    字典   dict  {"name":"jake"}




3.type()函数
可以获取变量的数据类型
type(变量) 
需要在变量的类型在控制台显示 需要使用print输出
print(type(变量))

"""
#整型
age=18
type(age)
print(type(age))
#浮点型
heigh=8.12
type(heigh)
print(type(heigh))
#布尔类型
isMEN=True
print(type(isMEN))
#字符串
num="nihao"
print(type(num))