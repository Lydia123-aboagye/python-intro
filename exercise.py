#variables
name = "Lydia" 
age = "19"
contry = "Ghana"
print(f"My name is {name}, I am {age} years old and I'm from {contry}")

#birth year to current age
birth_year = int(input("Enter your birth year:"))
current_year =  2026
calculated_age = current_year - birth_year
print(f"Your age is {calculated_age}")

#string to intrger
number = "25"
converted_number = int(number)
print(converted_number)

#remainder
remainder = 17 % 3
print(f"Remainder is {remainder}")

#area of a rectangle
length = 6
widht = 3
area_rectangle = length * widht
print(f"Area of a rectangle: {area_rectangle}")

#Swapping the values of two variables
a = 20
b = 30
a, b = b, a
print(a, b)

#area of a circle
radius = 5
pi = 3.142
area = pi*radius*radius
print("Area of circle is", {area})

#checking if a number is positive or negative
num = float(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num > 0:
    print("Negative")
else:
    print("Zero")

#1 to 10 with for loop
for i in range(1, 11):
    print(i)

#even numbers 1 to 20
for i in range(2,21,2):
    print(i)

#list of five fruits
fruits = ["apple","strawberry","cherry","banana","orange"]

#printig first and last item
fruits = ["grapes","orange","apple","kiwi","cherry"]
print(fruits[0])
print(fruits[-1])


#adding a new item
fruits.append("blueberry")
print(fruits)

#removing an item
fruits.remove("orange")
print(fruits)

#largest number in a list
num = (7,6,17,87,3,10)
largest = max(num)
print("Largest number is",{largest})

#counting how many times a numbr appears in a list
nums = [1,2,8,2,3,2,5,8,2,9,2]
print(nums.count(2))




