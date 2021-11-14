# ########################    Dictionary Project

login={}

for i in range(2):
    num1=int(input('1.login \n2.signup \n'))
    if num1 == 1:
        num2=input("nomber  ")
        if num2 in login.keys():
            print(login)
            break
        print("Create Account")
    else:
        signup={}
        print("please create your account")
        name=input("Username  ")
        email=input('Email   ')
        passw=input("Password  ")
        cont=input("number  ")
        signup['name']=name
        signup['email']=email
        signup["password"]=passw
        login[cont]=signup
        print(login)