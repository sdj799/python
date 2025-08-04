# panel Data 에서 나온 이름
# 표 형태의 데이터를 쉽고 강력하게 다를수 있게 해주는 라이브러리
# 엑셀의 Python 버전

import pandas as pd  # 판다스 라이브러리를 pd라는 별명으로 불러오기
import numpy as np   # 넘파이 라이브러리를 np라는 별명으로 불러오기

# Series: 판다스의 1차원 데이터 구조 (엑셀의 한 열과 비슷함)
# 추가: Series는 인덱스(행 이름)와 값으로 구성된 1차원 배열입니다.
# 리스트와 다른 점은 각 값에 이름(인덱스)을 붙일 수 있다는 것입니다.

print(" === Series ===")

# 1. 리스트로 Series 만들기
scores = pd.Series([85, 92, 78,  97],                    # 실제 점수 데이터 (값들)
                   # 각 점수에 해당하는 학생 이름 (인덱스)
                   index=["김철수", "이영희", "박민수", "최지영"],
                   name="수학점수")                         # Series 전체의 이름

print("1) 리스트로 만든 Series")
print(scores)
print(f"타입: {type(scores)}")
print()

# 추가: index 매개변수로 각 값에 의미있는 이름을 붙일 수 있습니다.
# name 매개변수로 Series 전체에 이름을 붙일 수 있습니다.

# 2. 딕셔너리로 Series 만들기
grade_dict = {"A": 90, "B": 80, "C": 70, "D": 60}  # 등급과 점수를 매핑한 딕셔너리
grade_series = pd.Series(grade_dict,                 # 딕셔너리를 Series로 변환
                         name="등급별_점수")            # Series에 이름 붙이기

print("2) 딕셔너리로 만든 Series")
print(grade_series)
print(f"타입: {type(grade_series)}")
print()

# 추가: 딕셔너리로 Series를 만들면 key가 인덱스, value가 값이 됩니다.
# 이미 key-value 쌍이 있는 데이터를 Series로 만들 때 유용합니다.

# 3. Numpy 배열로 Series 만들기
np_array = np.random.randint(70, 98, 5)  # 70부터 97까지 랜덤한 정수 5개 생성
print("np_array:", np_array)
random_scores = pd.Series(np_array,                              # numpy 배열을 Series로 변환
                          # 학생1, 학생2, ... 형태의 인덱스 생성
                          index=[f"학생 {i + 1}" for i in range(5)],
                          name="랜덤점수")                          # Series 이름 설정

print("3) Numpy로 만든 Series")
print(random_scores)
print(f"타입: {type(random_scores)}")
print()

# 추가: numpy의 random 함수를 사용하면 가짜 데이터를 쉽게 만들 수 있습니다.
# randint(최솟값, 최댓값+1, 개수) 형태로 사용합니다.
# 리스트 컴프리헨션 [f"학생 {i + 1}" for i in range(5)]로 반복적인 이름을 자동 생성할 수 있습니다.

print(" === Series 기본 속성들 ===")
# Series의 다양한 정보를 확인하는 속성들
print(f"값들:  {scores.values}")      # 실제 데이터 값들만 numpy 배열로 반환
print(f"인덱스:  {scores.index}")     # 인덱스(행 이름)들 반환
print(f"크기:  {scores.size}")        # 데이터의 개수
print(f"데이터 타입:  {scores.dtype}")  # 데이터의 자료형 (int64, float64 등)
print(f"이름:  {scores.name}")        # Series의 이름

# Series의 이름을 나중에 변경할 수 있음
scores.name = "3반 수학 점수"
print(f"이름:  {scores.name}")
print()

# 인덱스에도 이름을 붙일 수 있음
scores.index.name = "학생이름"
print(f"{scores}")
print()

# 추가: Series는 values, index, size, dtype, name 등의 속성을 가집니다.
# 이 속성들을 통해 Series의 구조와 정보를 파악할 수 있습니다.
# name과 index.name은 언제든지 변경할 수 있습니다.

print(" === Series 데이터 접근 ===")
# 단일 값 접근 - 딕셔너리처럼 대괄호 안에 인덱스 이름 입력
print("김철수의 점수:", scores["김철수"])

# 여러 값 접근 - 대괄호 안에 리스트로 여러 인덱스 이름 입력
print("김철수와 박민수의 점수:")
print(scores[["김철수", "박민수"]])
print()

# 추가: 단일 값 접근은 scores["인덱스이름"] 형태로 사용합니다.
# 여러 값 접근은 scores[["인덱스1", "인덱스2", ...]] 형태로 리스트를 안에 넣습니다.
# 대괄호가 두 개인 이유는 바깥쪽은 Series 접근, 안쪽은 인덱스 리스트이기 때문입니다.

# 조건을 사용한 데이터 필터링
high_scores = scores[scores > 80]  # 80점보다 큰 점수들만 선택
print("80점 초과 학생들:")
print(high_scores)
print()

# 추가: scores > 80은 각 값이 80보다 큰지 True/False로 판단한 결과를 반환합니다.
# 이 결과를 다시 scores[]에 넣으면 True인 값들만 선택됩니다.
# 이를 '불린 인덱싱(Boolean Indexing)'이라고 합니다.

# Series에 연산 적용 (모든 값에 동일한 연산 적용)
bonus_scores = scores + 10  # 모든 점수에 10점씩 추가
print("보너스 점수 (모든 점수 + 10):")
print(bonus_scores)
print()

# 추가: Series에 숫자를 더하면 모든 값에 그 숫자가 더해집니다.
# 이를 '브로드캐스팅(Broadcasting)'이라고 하며, +, -, *, / 모든 연산이 가능합니다.

print(" === Series 통계 함수 ===")
# Series에서 자주 사용하는 통계 계산 함수들
print(f"평균 : {scores.mean():.1f}")      # 평균값 계산 (소수점 1자리까지 표시)
print(f"최댓값 : {scores.max()}")         # 최댓값
print(f"최솟값 : {scores.min()}")         # 최솟값
print(f"표준편차 : {scores.std():.2f}")    # 표준편차 (소수점 2자리까지 표시)
print(f"합계 : {scores.sum()}")          # 모든 값의 합

# 추가: 판다스는 다양한 통계 함수를 제공합니다.
# mean(), max(), min(), std(), sum() 외에도 median(), var(), count() 등이 있습니다.
# :.1f, :.2f는 소수점 자릿수를 제한하는 문자열 포매팅입니다.

print("\n" + "="*50)
print("연습 문제")
print("="*50)

# 연습 문제 1: 과일 가격 데이터
fruits = pd.Series({
    '사과': 1500,
    '바나나': 2000,
    '오렌지': 1800,
    '포도': 3000,
    '딸기': 2500
})

print("과일 가격 데이터:")
print(fruits)
print()

# 1. 바나나 가격 출력
print("1. 바나나 가격:")
print(f"바나나 가격: {fruits['바나나']}원")
# 추가: 딕셔너리처럼 fruits['바나나']로 특정 과일의 가격에 접근할 수 있습니다.

# 2. 가장 비싼 과일의 가격
print("\n2. 가장 비싼 과일의 가격:")
max_price = fruits.max()  # 최댓값 구하기
print(f"가장 비싼 과일 가격: {max_price}원")
# 추가: max() 함수는 Series에서 가장 큰 값을 반환합니다.

# 3. 평균 가격
print("\n3. 평균 가격:")
avg_price = fruits.mean()  # 평균값 구하기
print(f"과일 평균 가격: {avg_price:.1f}원")
# 추가: mean() 함수는 모든 값의 평균을 계산합니다.

# 4. 2000원 이상인 과일들
print("\n4. 2000원 이상인 과일들:")
expensive_fruits = fruits[fruits >= 2000]  # 2000원 이상인 과일들만 필터링
print(expensive_fruits)
# 추가: fruits >= 2000은 각 가격이 2000 이상인지 확인하고,
# fruits[조건]으로 조건을 만족하는 데이터만 선택할 수 있습니다.

print("\n" + "="*50)

# 연습 문제 2: 수학 점수 데이터
math_scores = pd.Series({
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최지영': 96,
    '정다운': 83,
    '홍길동': 89,
    '신짱구': 74
})

print("수학 점수 데이터:")
print(math_scores)
print()

# 1. 전체 평균 점수
print("1. 전체 평균 점수:")
avg_score = math_scores.mean()  # 전체 평균 계산
print(f"전체 평균 점수: {avg_score:.1f}점")
# 추가: mean() 함수로 모든 학생의 평균 점수를 구할 수 있습니다.

# 2. 90점 이상인 학생 수
print("\n2. 90점 이상인 학생 수:")
high_scorers = math_scores[math_scores >= 90]  # 90점 이상인 학생들
high_score_count = len(high_scorers)  # 개수 세기
print(f"90점 이상인 학생 수: {high_score_count}명")
print("90점 이상인 학생들:")
print(high_scorers)
# 추가: len() 함수로 Series의 길이(개수)를 셀 수 있습니다.
# 또는 high_scorers.count()를 사용해도 같은 결과를 얻을 수 있습니다.

# 3. 80점 미만인 학생들의 이름
print("\n3. 80점 미만인 학생들:")
low_scorers = math_scores[math_scores < 80]  # 80점 미만인 학생들
low_scorer_names = low_scorers.index.tolist()  # 인덱스(이름)를 리스트로 변환
print(f"80점 미만인 학생들: {low_scorer_names}")
print("상세 점수:")
print(low_scorers)
# 추가: Series.index는 인덱스(여기서는 학생 이름)에 접근합니다.
# tolist()는 인덱스를 파이썬 리스트로 변환합니다.

# 4. 가장 높은 점수를 받은 학생의 이름
print("\n4. 가장 높은 점수를 받은 학생:")
max_score = math_scores.max()  # 최고 점수
max_student = math_scores.idxmax()  # 최고 점수를 받은 학생의 인덱스(이름)
print(f"최고 점수: {max_score}점")
print(f"최고 점수 학생: {max_student}")
# 추가: idxmax() 함수는 최댓값을 가진 인덱스(이름)를 반환합니다.
# 반대로 idxmin()은 최솟값을 가진 인덱스를 반환합니다.

print("\n" + "="*50)
print("추가 설명")
print("="*50)
print("""
Series의 주요 특징과 활용법:

1. 생성 방법:
   - 리스트: pd.Series([값들], index=[인덱스들])
   - 딕셔너리: pd.Series({키: 값})  
   - numpy 배열: pd.Series(np_array)

2. 데이터 접근:
   - 단일 값: series['인덱스']
   - 여러 값: series[['인덱스1', '인덱스2']]
   - 조건부: series[series > 값]

3. 유용한 함수들:
   - 통계: mean(), max(), min(), sum(), std()
   - 인덱스 관련: idxmax(), idxmin()
   - 정보 확인: .values, .index, .size, .dtype

4. 연산:
   - 모든 값에 동일 연산: series + 10, series * 2
   - Series끼리 연산도 가능: series1 + series2

Series는 판다스의 기본 단위로, DataFrame의 각 열이 Series입니다.
따라서 Series를 잘 이해하면 DataFrame 사용이 훨씬 쉬워집니다!
""")