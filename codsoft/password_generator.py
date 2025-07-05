import random
list1=[1,2,3,4,5,6,7,8,9]
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3=['@','#','$','%','!','^','&','*','(',')']
print("welcome to password generator")
x=int(input("how many numbers you want in your password"))
y=int(input("how many letters you want in your password"))
z=int(input("how many symbols you want in your password"))
password=""
for i in range(0,x):
    numbers=random.choice(list1)
    password+=str(numbers) 

for i in range(0,y):
    letters=random.choice(list2)
    password+=letters

for i in range(0,z):
    symbol=random.choice(list3)
    password+=symbol

print("your password is here:",  password)        