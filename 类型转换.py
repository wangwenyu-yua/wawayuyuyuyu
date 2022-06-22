
"""
根据代码的需要 将一种数据转换另一种数据类型将 input输入得到的数字转换为整型

语法：
变量=要转换的类型(原数据)
1.数据原来是说明类型
2.你要转换为说明类型


注意点：数据类型转换，不会改变原来的数据类型，会生成一个新的数据类型
int的转换 
int() 将其他类型转换为int类型
    1.可以将float类型转换为整型
    2.可以将整数类型的字符串 转换为 整型 3 123
float() 将其他类型转换为浮点型
    1.可以将int类型转换为浮点型  float(3)--->3.0
    2.可以将数字类型的字符串（整数类型和小数类型）转换为浮点型
str() 
    将其他类型都可以使用str()将其转换为字符串，一般是直接加引号

"""

#将input 输入的刀片的数字转换为整型
age =input("请输入您的年龄")
print("age本来的类型", type(age))

#类型转换
age1=int(age)
print("转换后age类型", type(age))
print("转换后age1的类型", type(age1))

