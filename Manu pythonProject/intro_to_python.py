#single line comment
"""
multiline comment example
multiline comment example
multiline comment example
"""
#variables and the different data types
student_name="Kamau" #string
student_age=20 #integer
student_height=6.1 #float
is_male=True #boolean

print(student_name,student_age,student_height)

firstname="kamau"
secondname="Sydney"
print(firstname+" "+secondname)

firstname="Manu"
secondname="10"
fullname=firstname+" "+str(secondname)
print(fullname)

price1="200"
price2=500
total=int(price1) + price2
print(total)

#operators
#Arithmetic operators
# + - * / %  ** //

print(2/5)
print(2%5)
t=20
if t%2==0:
    print("even")
else:
    print("odd")

#Comparison operators
print(5!=2)

#logical operators
#amd or
age=20
nationality="North America"
if nationality=="Kenya" and age==35:
    print("You can be president")
else:
    print("You are not president")

student1="present"
student2="absent"
if student1=="present" or student2=="present":
    print("pass")
else:
    print("not pass")

z=int(input("Enter a number:"))
if  z%2==0:
    print("even")
else:
    print("odd")

#illustration of the elif
b=5
if b>3:
    print("the value in b is greater than 3")
elif b==3:
    print("the value in b is equal to 3")
else:
    print("the value in b is less than 3")

city=input("Which city are you from:" )
if city=="Nairobi":
    print("elligible")
elif city=="Kisumu":
    print("elligible")
elif city=="Mombasa":
    print("elligible")
else:
    print("inelligible")

j=int(input("Enter a number:"))
k=int(input("Enter a number:"))
operator=int(input("Enter the operation:"))
if operator==1:
    print(j+k)
elif operator==2:
    print(j-k)
elif operator==3:
    print(j*k)
elif operator==4:
    print(j/k)
else:
    print("invalid")
