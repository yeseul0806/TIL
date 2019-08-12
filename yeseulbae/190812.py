# 1. total 함수
# 2. avarage 함수
# 누산 - for
# 초기값

def total(scores):
    total_score = 0
    for i in range(0, len(scores)):
        total_score +=scores[i]
    return total_score

def test_total_with_empty():
    assert total([]) == 0

def test_total_only_one():
    assert total([80]) == 80

def test_total_only_two_subjects():
     assert total([80, 20]) == 100

def test_total_with_large_case():
    assert total([80, 20, 60, 70, 30]) == 80 + 20 + 60 + 70 + 30
    assert total([80, 20, 60, 70, 30]) == total([80 + 20 + 60 + 70]) + 30
    assert total([80, 20, 60, 70, 30]) == total([80 + 20 + 60]) + 100

def test_total_with_empty():
    assert total([]) == 0


