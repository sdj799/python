import pandas as pd
import numpy as np

# panel Data 에서 나온 이름
# 표 형태의 데이터를 쉽고 강력하게 다룰수 있게 해주는 라이브러리
# 엑셀의 python 버전

# Series

scores = pd.Series([85,92,78,97], index=["김철수", "이영희", "박민수", "최지영"], name="수학점수")
print(scores)
print(f"타입: {type(scores)}")

grade_dict = {"A":90,"B":80,"C":70,"D":60}
grade_series = pd.Series(grade_dict,  name="등급별 점수")

print(grade_series)
print(f"타입: {type(grade_series)}")

np_array = np.random.randint(70,98,5)
print("np_array", np_array)
random_scores = pd.Series(np_array, index=[f"학생 {i+1}" for i in range(5)], name="랜덤점수")

print(random_scores)
print(f"타입: {type(random_scores)}")

print(f"값들: {scores.values}")
print(f"인덱스: {scores.index}")
print(f"크기: {scores.size}")
print(f"데이터 타입: {scores.dtype}")
print(f"이름: {scores.name}")

scores.name = "3반 수학 점수"
print(f"이름: {scores.name}")
scores.index.name = "학생이름"
print(f"인덱스: {scores}")
# 단일 값 접근
print(scores["김철수"])
# 여러 값 접근
# 인덱스 안에 리스트로 작성
print(scores[["김철수", "박민수"]])

high_scores = scores[scores > 80]
print(high_scores)

bonus_scores = scores + 10
print(bonus_scores)

print(f"평균: {scores.mean():.1f}")
print(f"최댓값: {scores.max()}")
print(f"최솟값: {scores.min()}")
print(f"표준편차: {scores.std():.1f}")
print(f"합계: {scores.sum()}")

fruits = pd.Series({
    '사과': 1500,
    '바나나': 2000,
    '오렌지': 1800,
    '포도': 3000,
    '딸기': 2500
})
# 1. 바나나 가격 출력
print("바나나:", fruits["바나나"])
# 2. 가장 비싼 과일의 가격
print("비싼과일 가격:",  fruits.max())
# 3. 평균 가격
print("평균가격:",fruits.mean())
# 4. 2000원 이상인 과일들
print("2000원 이상:", fruits[fruits >= 2000])

math_scores = pd.Series({
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최지영': 96,
    '정다운': 83,
    '홍길동': 89,
    '신짱구': 74
})
# 1. 전체 평균 점수
print("전체 평균:", math_scores.mean())
# 2. 90점 이상인 학생 수
print("90점 이상인 학생 수:", math_scores[math_scores >= 90].size)
# 3. 80점 미만인 학생들의 이름
print("80점 미만 학생:", math_scores[math_scores < 80].index.tolist())
# 4. 가장 높은 점수를 받은 학생의 이름
print("가장 높은 점수를 받은 학생:",  math_scores.idxmax())