# 2배
def double(n):
    return n * 2


print(double(2))
print(double(4))


# 더하기
def add(x, y):
    return x + y


print(2, 3)
print(4, 5)


# BMI
def bmi(w, h):
    return w / (h ** 2)


print(bmi(60, 1.60))


# 계승
def factorial(n):
    accumulator = 1
    for i in range(1, n + 1):
        accumulator *= i
    return accumulator


for i in range(1, 10 + 1):
    print(factorial(i))


# 구구단
def gugu(a):
    z = []
    for i in range(1, 10):
        print(a, "*", i, "=", a * i)

gugu(3)

# 연습문제


def total(score):
    t_score=0
    for i in score:
        t_score+=i
    return t_score

scores=[80,100,70,90,40]

print(total(scores))

def avg(value):
    t_score=0
    for i in value:
        t_score+=i
    avg=t_score/len(value)
    return avg

print(avg(scores))
