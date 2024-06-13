# Datatype

number = 60 # Int
num =45.36 # Float
greeting ="Hello there" # str
isPythonIntresting = True # boolean

# list
fruits = ["banana","mango", "apple"]
cars =("bwd", "mercedes","toyota", "v8") # tuple
countries ={"Kenya","Tanzania","Uganda"} # set
student ={
    "firstname" :"Gold",
    "age" : 19,
    "course" : "MIT",
    "nationality":"Kenyan"
}# Dictionary


print(student["firstname" ])
print(countries)
print(cars)
print(num)
print(isPythonIntresting)
print(fruits)

#Determinind data type
print (type (isPythonIntresting))
print(type (cars))


# Typecasting is converting one data type to another
print(int(num))
print(float(number))