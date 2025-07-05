flag=True
while (flag):
    def addition(num1,num2):
        print("your addition is as",num1+num2)
    

    def subtraction(num1,num2):
        print("your subtraction is as",num1-num2)
    

    def multiplication(num1,num2):
        print("your multiplication is as",num1*num2)  
    

    def division(num1,num2):
        print("your division is as",num1/num2)
    
    
    num1=int(input("enter your first number"))
    num2=int(input("enter your second number"))


    print("1_addition")
    print("2_subtraction")
    print("3_multiplication")
    print("4_division")
    choice=int(input("enter your choice 1,2,3,4"))

    if(choice==1):
        addition(num1,num2)

    elif(choice==2):
        subtraction(num1,num2)

    elif(choice==3):
        multiplication(num1,num2)

    elif(choice==4):
        division(num1,num2)

    z=int(input("begin with next calculation \n 1_next calculation \n 2_end calculation"))   
    if(z==1):
        flag=True 
    elif(z==2):
        flag=False    
        
