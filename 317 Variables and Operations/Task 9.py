# Task 9: Recipe Scaler
# Write a program that:

# Stores ingredients for a chocolate chip cookie recipe that
# serves 4 people (flour in grams, butter in grams, sugar in grams,
# number of eggs, chocolate chips in grams, vanilla in teaspoons)
# Work out the scaling factor as the user wants to cook for 6 people
# instead
# Scale all ingredients proportionally using the calculated factor
# Display the new ingredient amounts

names = ['flour','butter','sugar','eggs', 'chocchips','vanilla']
orig = [100,100,100,4,60,3]
newOrig = []

scalingFactor = 6/4

for index in range(len(orig)):
    newOrig.append(orig[index] * scalingFactor)
    print(names[index] + ":" +str(newOrig[index]))