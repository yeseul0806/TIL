# list, dictionary, set

def test_list():
    scores = [10, 20, 30]
    assert scores[0] == 10
    assert scores[1] == 20
    assert scores[2] == 30
    #append
    scores.append(5)
    assert scores == [10, 20, 30, 5]
    # 데이터 바꾸기
    scores[0] = 0
    assert scores == [0, 20, 30, 5]

# 키를 이용해서 찾는 딕셔너리
def test_dictionary():
    korean = '국어'
    scores = {
        '국어' : 10,
        '영어' : 20,
        '수학' : 30
    }
    assert scores['국어'] == 10
    assert scores['영어'] == 20
    assert scores['수학'] == 30

def test_dictionary2():
    korean = '국어'
    scores = {
        korean : 10,
        20 : 10
    }
    assert scores[korean] == 10
    assert scores['국어'] == 10
    assert scores[20] == 10


def test_set():
    subjects = {'국어', '영어', '수학'}
    assert '국어' in subjects
    assert '음악' not in subjects
    assert '음악' in subjects.union({'음악'}) #합집합 union
    subjects.add('기가')