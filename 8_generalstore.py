import time

print ("General store is open from 10AM to 5PM. Please Hurry!")

time.sleep(2)

order = input ("What would you like to buy:\n medicine \n candy \n fruit \n")

if order == "medicine":
  price = 10
  amount = int(input ("How much medicine would you like to purchase"))
  result = (price * amount)
  print ("Your bill would be £{}".format(result))

if order == "candy":
  price = 7
  amount = int(input ("How much candy would you like to purchase"))
  result = (price * amount)
  print ("Your bill would be £{}".format(result))

if order == "fruit":
  price = 5
  amount = int(input ("How much fruit would you like to purchase"))
  result = (price * amount)
  print ("Your bill would be £{}".format(result))

else:
  print ("invalid input")