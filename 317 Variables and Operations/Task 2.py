# Task 2: Shopping Calculator
# Create a program that calculates the total cost of shopping items:

# Store the price of 3 different items in variables
# Store the quantity of each item purchased
# Calculate and display the total cost for each item
# Calculate and display the grand total

item1 = 0.10
item2 = 0.07
item3 = 4.55
q1 = 10
q2 = 88
q3 = 3
tc1 = item1*q1
tc2 = item2*q2
tc3 = item3*q3
print("Total cost of item 1: £"+str(tc1))
print("Total cost of item 2: £"+str(tc2))
print("Total cost of item 3: £"+str(round(tc3,2)))
totalCost = tc1+tc2+tc3
print("Overall cost: £"+str(totalCost))
