#Datatypes in python
#Integers - whole numbers
a = 34

#Float - decimal numbers
b = 28.95

#String - anything in speech marks - set of characters
c = "Hello"
d = "100"
e = "45.8"

#Boolean - True or False
f = True
g = False

#Activity 1
x = 20
y = 5
z = x + y
print(z)

#String concatenation - joining strings together
p = "20"
q = "5"
r = p + q
print(r)
 
#Activity 2
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))
result = num1 + num2
print(result)

#Activity 3
"""0 to 4 - toddler
4 to 13- kid
13 to 18 - teenage
19 to 100 - adult
rest all values - invalid input """

age = int(input("How old are you ?"))
if age > 0 and age <= 4:
  print("You are a toddler.")
elif age > 4 and age <= 13:
  print("You are a Teenager.")
elif age > 13 and age < 18:
  print("You are a Teenager.")
elif age >= 18 and age <= 120:
  print("You are an adult.")
else:
  print("Invalid age./. Please enter valid age.")

#Acivity 4
age1 = int(input("Enter the age : "))
result = age1 + 10
print("After 10 years , you r age will be", result)

#Additional
print("\n")
#For loop
#range(start,stop,step)
#Asc
for i in range(1, 11, 2):
  print(i)

print("\n")
#Des
for i in range(9, 0, -2):
  print(i)
  
#Leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

