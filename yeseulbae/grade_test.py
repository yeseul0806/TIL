from grade import class_grade
from grade import class_grade_dic

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

#단일 점수를 넣을 떄
def test_class_grade():
    assert class_grade(80, '국어') == '국어 : A'
    assert class_grade(45, '수학') == '수학 : C'


print(class_grade_dic(class_scores, 0, '국어'))
print(class_grade_dic(class_scores, 1, '영어'))
# 딕셔너리를 넣을 때