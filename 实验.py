def  checkname(username,password):
    
 
    if len(username)>=5 and len(username) <= 8:
        if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
            if len(password)>=8 and len(password) <=12:
                return True     
            else:
                return"密码不符合规范"
        else:
            return "账号信息必须以小写字母开头"
    else:
        return "您的账号不符合规则。请输入5-8位账号"       
checkname("zhangdang","12345678")
# username=input("请输入您的账号")
# password=input("请输入您的密码")
# if checkname(username)==True:
#             if len(password) >= 8 and len(password) <=12:
#                 print("注册成功",{username:password})
#             else:
        
#                 print("密码必须是8-12位")
# else:
#             print(checkname(username))