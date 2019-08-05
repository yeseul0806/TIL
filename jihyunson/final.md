# 과제 1

## 성적 총합 & 평균 구하기
```py
my_scores = [30, 90, 80, 40,50]
class_scores = 
[30, 90, 80, 40, 50]
[100, 100, 100, 100, 100]   
[0, 90, 30, 30, 20]
```

총합 Answer:
```py
my_scores = [30, 90, 80, 40,50]
sum = 0
for i in range(0, 5):
    sum += my_scores[i]
print(sum)
```
or class_scores의 총합일 경우:
```py
class_scores = [[30, 90, 80, 40, 50], [100, 100, 100, 100, 100], [0, 90, 30, 30, 20]]
sum = 1
for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        sum += class_scores[i][j]
print(sum)
```

평균 Answer
```py
class_scores = [[30, 90, 80, 40, 50], [100, 100, 100, 100, 100], [0, 90, 30, 30, 20]]
sum = 0
for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        sum += class_scores[i][j]
        average = sum/(len(class_scores[i])*len(class_scores))
print(average)
```

## 구구단 출력하기 
```py
2 * 1 = 2
2 * 2 = 4
9 * 8 = 72
9 * 9 = 81
```

Input Answer:
```py
a = input("What is the first number? Pick from 1-10")
b = input("What is the second number? Pick from 1-10")
mult = int(a)*int(b)
print(mult)
'''