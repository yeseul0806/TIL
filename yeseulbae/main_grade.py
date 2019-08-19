from grade import class_grade
from grade import class_grade_dic

def main():
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
    grade = []
    for i in range(len(class_scores)):
        for j in ['국어', '영어', '수학']:
            x  = class_grade_dic(class_scores, i , j)
            grade.append(x)
    print(grade)

main()