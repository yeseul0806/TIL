# 20190812 homework


class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]


def class_total(class_scores, a):
     total = 0
     for i in range(0, len(class_scores)):
         total +=class_scores[i][a]
     return total

print(class_total(class_scores, '국어'))
assert class_total(class_scores, '국어') == 170

def class_total_all(class_scores):
    total = 0
    for i in range(0, len(class_scores)):
        total += sum(class_scores[i].values())
    return total

assert class_total_all(class_scores) == 430