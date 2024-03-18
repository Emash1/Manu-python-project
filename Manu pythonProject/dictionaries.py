#dictionaries
#data is stored in key values paries
#ie key:value

cardata={
    "model":"Mercedes",
    "brand":"C200",
    "YOM":2022
}

print(cardata["brand"]) #accessing values in a dictionary we use the key
cardata["alloys"]="contains" #adding data to a dictionary
print(cardata)

cardata["brand"]="S550"
print(cardata)