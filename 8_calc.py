import time

choice = input("What operation do you want to use \n1. Addition + \n2. Subtraction - \n3. Multiplication x \n4. Division / \n")

time.sleep(2)


if choice == "1" or choice ==  "Addition":
  num1 = float(input("Enter the first number "))
  num2 = float(input("Enter the second number "))
  total = num1 + num2
  print("{} + {} = {} ".format(num1,num2,total))
elif choice == "2" or choice == "Subtraction":
  num1 = float(input("Enter the first number "))
  num2 = float(input("Enter the second number "))
  total = num1 - num2
  print("{} - {} = {} ".format(num1,num2,total))
elif choice == "3" or choice == "Multiplication":
  num1 = float(input("Enter the first number "))
  num2 = float(input("Enter the second number "))
  total = num1 * num2
  print("{} x {} = {} ".format(num1,num2,total))
elif choice == "4" or choice == "Division":
  num1 = float(input("Enter the first number "))
  num2 = float(input("Enter the second number "))
  total = num1 / num2
  print("{} ÷ {} = {} ".format(num1,num2,total))
else:
  print("Invalid input. Pls enter the value from 1 to 4")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  