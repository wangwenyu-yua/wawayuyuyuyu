"""class 后面跟类的名字 声明类的名字  类的名字首字母必须大写  
面向对象编程 类就是我们的对象 
类里面所有的方法 都必须要传一个参数  叫做self
默认属性方法 __int__来接受参数
每个类里面的方法，第一个参数必须是self
class 声明类

"""
class Girlfriend():
    def __init__(self,sex,high,weight,hair,age):#初始化
        self.sex=sex
        self.high=high
        self.weight=weight
        self.hair=hair
        self.age=age


    def caiyi(self,num):
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"22的女朋友开始了胸口碎大石之")
        if num==1:
            print("胸口碎大石")
        elif num==2:
            print("唱跳")
        else:
            print("敲代码")


    def chuyi(self):
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"22的女朋友开始了技能之")
        print("川菜")
        print("西餐")



    def work(self):
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了工作")
        print("程序员")

#类的实例化
wawayu=Girlfriend("男","183","90kg","锡纸烫","32")
wawayu.caiyi(1)
wawayu.work()
print(wawayu.high)


class Car():
    def __init__(self,pingpai,color,neishi,jilun,):
        self.pingpai=pingpai
        self.color=color
        self.neishi=neishi
        self.jilun=jilun
    def bainxing(self):
        print("车子变身")
    def fly(self):
        print("车子开始起飞")
    

zhangsan=Car("奔驰","五颜六色","豪华","独轮车")
zhangsan.bainxing()

"""
类的两个属性
1、继承
2、重写（也叫多态）

"""
class Girl(Girlfriend):
    def work(self):
        print("修电脑")

    pass
wawayu=Girl("nv","172","85kg","black","88")
wawayu.work()







"""  上述例子中  
object  祖宗类
Girl属于子类
GirlFriend属于是父类


"""


"""
python文件的读写
"""