#creating a function in python
def is_even(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


#calling a function
is_even(99)

#function2
def printEmobilis():
    for i in range(10):
        print(i+1,"Emobilis")

printEmobilis()

#function3
def printName(x="Kelvin"):
    for i in range(10):
        print(x)

printName("Sidney")
printName("Jude")
printName()

#function4
def getModulus(y,x):
    return y%4

z=getModulus(5,2)+90
print(z)