"""names=["Dion","Sindhu","Oli","Remi"]
print(names)

#index - starts with 0
print(names[0])
print(names[3])

for i in names:
  print(i)

#Negative indexing - starts from end (-1)
print(names[-1])

print(len(names))

#Adding values to the list - to the last of the list
names.append("Jack")
print(names) 	

names.insert(2,"John")
print(names)

#remove - from last
names.pop()
print(names)

names.pop(2)
print(names)

x=[23,90,19,45,61,100]
x.sort()
print(x)

x.sort(reverse=True)
print(x)

x.reverse()
print(x)

print(x[1])

#Slicing
print(x[1:4])

#from start
print(x[:4])

#till end
print(x[3:])

#random
import random

i=random.randint(1,100) #random value withing the given range
print(i)

j=random.random() #any random value from 0 to 1
print(j)

k=["Hi","Hello",23,45,"Coding",True]
m=random.choice(k) #pick random value from a list or string
print(m)

name="ReyanPrakash"
print(random.choice(name))

"""

#Password generator
import random
import time

#list

letters = ["A","B","c","D","E","F","G","H","I","K","L","M",
"N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"a","b","c","d","e","f","g","h","i","l","k","l","m", "n", "o",
"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = [
  "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{",
  "}", "[", "]", "|", "<", ">"
]

#random.choice - select any random value from list or string
a = random.choice(letters)
b = random.choice(letters)
c = random.choice(letters)

d = random.choice(symbols)
e = random.choice(symbols)
f = random.choice(symbols)

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

password = str("A strong password is {}{}{}{}{}{}{}{}".format(
  a, d, num1, b, e, num2, c, f))
print(password)

#To create infinte loop
while True:
  choice = input("Do you want another password ? Y/N ")
  if choice == "Y":
    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)

    d = random.choice(symbols)
    e = random.choice(symbols)
    f = random.choice(symbols)

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    password = str("A strong password is {}{}{}{}{}{}{}{}".format(
      a, d, num1, b, e, num2, c, f))
    print(password)

    time.sleep(2)

  elif choice == "N":
    print("Thanks for your time !")
    exit()

  else:
    print("Invalid input. Please select Y or N.")
    
"""
password = input("Enter a password: ")

has_number = False

for ch in password:
    if ch.isdigit():
        has_number = True
        break

if len(password) >= 8 and has_number:
    print("Strong")
else:
    print("Weak")

"""



  
  