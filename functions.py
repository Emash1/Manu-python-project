def largest_number():
    x= [5,4,43,56,33]
    return max(x)
print(largest_number())

#No2
"""
my_list = [5,4,10,50,78,50,5,78]
repeated_element = []
for i in my_list:
    if my_list.count(i)>1:
        if i not in repeated_element:
            repeated_element.append(i)
print(repeated_element)
"""

#No3
#ADD ITEMS TO A TUPLE
fruits=("apple","banana","cherry")
y=("orange","watermelon")
fruits +=y
print(fruits)

#NO4
mydictionary ={
    "model":"S300",
    "Brand":"Merceedes",
    "YOM":"2020"
}
del mydictionary["model"]
print(mydictionary)

#NO5
v=mydictionary.values()
if "S300" in v:
    print("Exists")
else:
    print("Not exists")

fruits1={"apple","banana","mangoes"}
fruits2={"passion","orange","watermelon"}
fruits1.update(fruits2)
print(fruits1)

#converting lists to dictionaries
list1=["model","year","brand"]
list2=["harrier","2020","toyota"]
print("My list1 is",list1)
print("My list2 is",list2)
mydict=dict(zip(list1,list2))
print("My dict is",mydict)

my_list = [5,4,10,50,78,50,5]
repeated_element = []
for i in my_list:
    if my_list.count(i)>1:
        repeated_element.append(i)
        if len(repeated_element)>1:
            break(repeated_element[0])
print(repeated_element)