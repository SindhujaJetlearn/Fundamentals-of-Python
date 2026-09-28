import random,os,time
#os.environ['TERM'] = 'xterm'

print("Welcome to number guessing game")

time.sleep(3)
os.system('clear')

#First question
x = random.randint(10, 100)
y = random.randint(1, 10)

guess1 = 0
ans1 = 0
tries1 = 3

#Until you get correct ans and guess count should not go beyond 4
while ans1 != x * y and guess1 != 4:
  ans1 = int(input("What will be {} multiplied by {} ? ".format(x, y)))
  if ans1 == x * y:
    print("Congratulations ! You got it right !")
    break
  else:
    print("Incorrect ! You have  {} tries left".format(tries1))
    tries1 -= 1
    guess1 += 1

print("Next Question")
print("\n")

#Second question
a = random.randint(100, 1000)
b = random.randint(10, 100)

guess2 = 0
ans2 = 0
tries2 = 3

#Until you get correct ans and guess count should not go beyond 4
while ans2 != a * b and guess2 != 4:
  print("If a = {} and b = {} ".format(a, b))
  ans2 = int(input("What will be a multiplied by b ? "))
  if ans2 == a * b:
    print("Congratulations ! You got it right !")
    break
  else:
    print("Incorrect ! You have  {} tries left".format(tries2))
    tries2 -= 1
    guess2 += 1

print("Game over")
print("\n")
