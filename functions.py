# Inbuilt Functions
y = max(230, 6578, 12, 890)
print(y)

x = min(45, 67, 87, 13, 56)
print("The minimum value is", x)

z = pow(2, 3)
print(z)

#User-defined function
def student():
    print("Gold")
student() # Calling a function

def Person():
    print("Person is walking")
Person()

#Parameters and Arguments
def add(num1, num2):
    print(num1 + num2)

add( 34, 35)
add( 100, 89)

def Employee(fullname, age, email, maritalstatus, position ):
    print(fullname, age, email, maritalstatus, position)

Employee("Gold White",34,"goldy58@gmail.com", "Married","Admin")
Employee("Claris zion",33,"zion46@gmail.com", "Single","CEO")
Employee("Glory Akot",32,"Email", "Single","MD")
Employee("Kavesa Sweetnah",31,"Email", "Single","MD")