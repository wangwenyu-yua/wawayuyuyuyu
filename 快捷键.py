"""
fjdhskjdsfl


"""



name="小米"#可以使用input输入

age=18#可以使用input输入
height=1.71#可以使用input输入
stu_num=1
Num=90
print('我的名字是xx,年龄是xx,身高是xx,学号 xx, 本次考试的及格率是 xx%')
print(f'我的名字是{name},年龄是{age},身高是{height},学号{stu_num}, 本次考试的及格率是{Num}%')

#在字符串中想要输出换行用\n  转义字符
print(f'我的名字是{name},\n年龄是{age},\n身高是{height},学号{stu_num}, 本次考试的及格率是{Num}%')
print(f'我的名字是{name},\n年龄是{age},\n身高是{height},学号{stu_num}, 本次考试的及格率是{Num}%'.format(name,age,height,stu_num,Num))