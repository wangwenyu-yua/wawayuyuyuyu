"""
PYTHON文件的读写：


"""

# import time
# now=time.strftime("%y-%m-%d-%H:%M:%S")

# text=input("请输入今天的心情：")
# with open(" C:\日记.txt","w",encoding="utf8") as f:#w会清空之前所写的内容
#     f.write(now+"\n")
#     f.write(text+"\n")
#     f.write("--------------------------+\n")



import time
now=time.strftime("%y-%m-%d-%H:%M:%S")
text=input("请输入今天的心情：")
with open("E:\日记.txt","a",encoding="utf8") as f:#a代表追加内容的
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("--------------------------+\n")    
print("哈哈哈\t你还好吗")
print("hahahah\nhhhhhh")
"""
python制表符
\t:自动的增加tab的位置

\n：换行的效果
"""