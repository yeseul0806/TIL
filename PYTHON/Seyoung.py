my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

Total_score = class_scores[0][0] + class_scores[0][1] + class_scores[0][2] + class_scores[0][3] + class_scores[0][4]+ \
              class_scores[1][0] + class_scores[1][1] + class_scores[1][2] + class_scores[1][3] + class_scores[1][4] +\
              class_scores[2][0] + class_scores[2][1] + class_scores[2][2] + class_scores[2][3] + class_scores[2][4]

total1 = sum(class_scores[0][:])
total2 = sum(class_scores[1][:])
total3 = sum(class_scores[2][:])

print("Total_score =", Total_score)
print("Total 1 =", total1)
print("Total 2 =", total2)
print("Total 3 =", total3)


Total_sum = 0
n = 0
for i in range(0,len(class_scores)):
   for j in range(0,len(class_scores[i][:])):
       Total_sum += class_scores[i][j]
       n += 1

print("Total_sum =", Total_sum)
print("Total_avg =", Total_sum/n)




