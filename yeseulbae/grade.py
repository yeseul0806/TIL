

def class_grade(scores, subject):
    if scores >= 80:
        grade = subject + ' : ' + 'A'
    elif scores < 80 and scores >= 60:
        grade = subject + ' : ' + 'B'
    elif scores < 60 and scores >= 40:
        grade = subject + ' : ' + 'C'
    elif scores < 40 and scores >= 20:
        grade = subject + ' : ' + 'D'
    else:
        grade = subject + ' : ' + 'F'
    return grade

def class_grade_dic(scores, i , subject):

    if scores[i][subject] >= 80:
        grade = subject + ' : ' + 'A'
    elif scores[i][subject] < 80 and scores[i][subject] >= 60:
        grade = subject + ' : ' + 'B'
    elif scores[i][subject] < 60 and scores[i][subject] >= 40:
        grade = subject + ' : ' + 'C'
    elif scores[i][subject] < 40 and scores[i][subject] >= 20:
        grade = subject + ' : ' + 'D'
    else:
        grade = subject + ' : ' + 'F'

    return grade
