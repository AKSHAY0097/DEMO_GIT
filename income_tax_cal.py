"""Project name : INCOME-TAX CALCULATOR
Version         : 1.0
Devloper Name   : Akshay Sudhakar Kathar
Date            : 16-06-2022 """


name = input("ENTER YOUR NAME :")
age = int(input("ENTER YOUR AGE :"))
def asal(msal):
    res=msal*12
    return res
if age <60:
    def atax(asal):
        if asal<=250000:
            res=0
        elif asal<=500000:
            res=asal*5/100
        elif asal<=1000000:
            res=asal*20/100
        else:
            res=asal*30/100
        return res
if age >60:
    def atax(asal):
        if asal<=300000:
            res=0
        elif asal<=500000:
            res=asal*5/100
        elif asal<=1000000:
            res=asal*20/100
        else:
            res=asal*30/100
        return res
if age >80:
    def atax(asal):
        if asal<=500000:
            res=0
        elif asal<=500000:
            res=asal*5/100
        elif asal<=1000000:
            res=asal*20/100
        else:
            res=asal*30/100
        return res
msal=float(input("enter your monthly sal :"))
annual_sal= asal(msal)    
print("Income-tax-calculator by Akshay kathar".capitalize())
print("HI", name.capitalize(),"your annual sal is :",annual_sal)

annual_tax=atax(annual_sal)
print("Hi",name.capitalize(),"your annual tax is :",annual_tax)

monthly_tax=annual_tax/12
print(f"Hi {name.capitalize()} your monthly tax cutting is : {monthly_tax}")
