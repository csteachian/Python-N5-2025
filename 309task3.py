# Program 3 - Investigate and Modify
import random
price = [random.randint(1,10) for index in range(3)]
total = 0
for x in range(len(price)):
   total = total + price[x]
print('The total cost is: £' + str(total) )
print(price)

