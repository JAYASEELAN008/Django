
# class Calculator:
   
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         return self.a + self.b

#     def subtract(self):
#         return self.a - self.b

#     def multiply(self):
#         return self.a * self.b

#     def divide(self):
#         return self.a / self.b
# while True:
#     a=int(input("Enter the first value:")) 
#     b=int(input("Enter the second value:"))
#     options=input("Enter the add=1 sub=2 mul=3 div=4:")
#     calc = Calculator(a,b)
#     if options == "1":
#         print(calc.addition())
#     elif options =="2":
#         print(calc.subtract())
#     elif options =="3":
#         print(calc.multiply())
#     elif options =="4":
#         print(calc.divide())
#     else:
#         break

    
# print(calc)




class Coustomer:
    bankname="OJHA"
    def __init__ (self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("total available balance is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("you have insufficient balance")
        else:
            self.balance=self.balance-amount
            print("available balance is: ",self.balance)
            
print("welcome to",Coustomer.bankname)
name=input("enter your name")
data=Coustomer(name)
while True:    
    print("w-withdraw\nd-deposite\ne-exit")
    option=input("enter the operation you want to perform").lower()
    if option=='d':
        amount=float(input("enter the amout to be depositted:"))
        data.deposit(amount)
    elif option=='w':
        amount=float(input("enter the amout to be withdraw:"))
        data.withdraw(amount)
    elif option=='e':
        break
    else:
        print("the given input doesn't perform operation")
    
