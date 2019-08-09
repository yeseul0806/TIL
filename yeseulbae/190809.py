# assert 1 + 1 == 2 #성공한거는 안알려주고
# assert 1 + 1 == 4
#
#
# def double(n):
#     return n * 2 + 1
#
#
# def test_double():
#     assert double(2) == 4
#     assert double(1) == 2
#
#
# assert double(2) == 4
# assert double(1) == 2




 # def test_simple():
 #     assert 1 + 2 == 2



scores=[80, 100, 70, 90, 40]
scores2=[10,30]


def total_score(score):
    total = 0
    for i in score:
        total +=i
    return total

def test_total():
    assert total_score(scores) == 280
    assert total_score(scores) == 480
    assert total_score(scores2) == 40
    assert total_score([10, 20, 30]) == 60

def avarage_score(score):
    x = total_score(score)
    return x/len(score)

def test_average():
    assert avarage_score(scores) == 76
    assert avarage_score(scores2) == 20
    assert avarage_score([10, 30, 50]) == 30






