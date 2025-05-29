scores = [75, 82, 93, 65, 78]
highestScore = scores[0]
for index in range(1,len(scores)):
   if scores[index] > highestScore:
      highestScore = scores[index]

print("The highest score is", highestScore)