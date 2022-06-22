from asyncore import read


with open("E:/日记.txt","r",encoding="utf8") as f:
    text=f.readlines()
    print(text)
for i in text:
    print(i)
#您还