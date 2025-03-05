print()
homeHT = int(input("Enter the half time score for the home team: "))
awayHT = int(input("Enter the half time score for the away team: "))

print()
noGoalsScored = (homeFT + awayFT) - (homeHT + awayHT)
homeFT = int(input("Enter the full time score for the home team: "))
print("The number of goals scored after the half time break was: "+str(noGoalsScored))
awayFT = int(input("Enter the full time score for the away team: "))