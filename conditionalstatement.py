temprature = 32

if temprature < 25:
    print("It is cold")
elif temprature > 25:
    print("It is hot")
else:
    print("Normal temprature")
# A program that returns the largest number among three numbers
first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")

#A python program that checks whether a number is even or odd
first = 56
second = 23

if first % 2 == 0:
    print(first, "is even number")
else:
    print(first, "is odd number")

if second % 2 == 0:
    print(second, "is even number")
else:
    print(second, "is odd number")

    #or
number = 0
if number == 0:
    print("is neutral number")
elif number % 2 == 0:
    print("is even number")
else:
    print(number, "is odd number")

#A python program that returns the area of a rectangle
#A =if second % 2 == 0:
length = 20
width = 5
area = length * width
print("The area is", area)

#A python program that returns the area of a trapezium
#A =0.5 (a+b) * h
a = 7
b = 5
height = 10
area = 0.5 * (a + b) * height
print("The area is", area)
print(int(area))
