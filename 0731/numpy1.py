# numpy: 숫자 계산을 빠르고 쉽게 할 수 있도록 도와주는 라이브러리
import numpy as np  # np 라는 이름으로 numpy를 사용하겠다.

# ✅ 리스트를 이용한 연산 vs numpy 연산 비교

# 일반 리스트에서 각 요소를 2배로 만드는 방법 (반복문 사용)
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    result.append(num * 2)
print("result: ", result)  # [2, 4, 6, 8, 10]

# numpy 배열에서는 벡터 연산으로 간단히 처리 가능
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2
print("numpy result: ", result)  # [2 4 6 8 10]

# ✅ 두 리스트를 더하기

# 일반 리스트 덧셈 (인덱스 기반 반복)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print("result: ", result)  # [5, 7, 9]

# numpy 배열의 덧셈
list1 = np.array([1, 2, 3])
list2 = np.array([4, 5, 6])
result = list1 + list2
print("numpy result: ", result)  # [5 7 9]

# ✅ numpy 장점
# - 빠른 계산 속도
# - 적은 메모리 사용
# - 다양한 수학 연산 가능
# - 다차원 배열 지원

# ✅ 1차원 배열
list_1d = [1, 2, 3, 4, 5]
np_list_1d = np.array(list_1d)
print("1차원 배열: ", np_list_1d)
print("배열 타입: ", type(np_list_1d))  # <class 'numpy.ndarray'>

# ✅ 2차원 배열
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_list_2d = np.array(list_2d)
print("2차원 배열: ", np_list_2d)
print("배열 타입: ", type(np_list_2d))

# ✅ 데이터 타입 지정
np_list_float = np.array([1, 2, 3], dtype=float)
np_list_int = np.array([1.1, 2.2, 3.5], dtype=int)
print("실수 배열: ", np_list_float)  # [1. 2. 3.]
print("정수 배열: ", np_list_int)    # [1 2 3]

# ✅ 정수 인덱싱 예시 (특정 위치 값 가져오기)
# [
#     [1 (0,0), 2 (0,1), 3 (0,2)],
#     [4 (1,0), 5 (1,1), 6 (1,2)],
#     [7 (2,0), 8 (2,1), 9 (2,2)]
# ]
print("np_list_2d[[1, 1], [2, 2]]:", np_list_2d[[1, 1], [2, 2]])  # [6 6]
print("np_list_2d[[0, 1], [0, 2]]:", np_list_2d[[0, 1], [0, 2]])  # [1 6]
print("np_list_2d[[2, 1], [2, 1]]:", np_list_2d[[2, 1], [2, 1]])  # [9 5]
print("np_list_2d[[0, 2], [2, 0]]:", np_list_2d[[0, 2], [2, 0]])  # [3 7]

# ✅ 학생 성적 예시: 행과 열 인덱스를 이용한 점수 추출
# 국어 영어 수학
scores = np.array([
    [79, 80, 40],
    [75, 82, 70],
    [72, 84, 69]
])
rows = [1, 0, 2]
cols = [2, 1, 0]
print(scores[rows, cols])  # [70 80 72]

# ✅ 조건 필터링과 값 변경
arr1 = np.array([11, 20, 31, 40, 51])
print("arr1[arr1 > 31]:", arr1[arr1 > 31])        # [40 51]
print("arr1[arr1 % 2 == 0]:", arr1[arr1 % 2 == 0])  # [20 40]
arr1[arr1 > 31] = 0
print("arr1:", arr1)  # [11 20 31 0 0]
lists = [0, 2, 4]
print("arr1[lists]:", arr1[lists])  # [11 31 0]

# ✅ 0으로 채운 배열 만들기
zeros_array = np.zeros((2, 3))
print("zeros_array:", zeros_array)

# ✅ 1로 채운 배열 만들기
ones_array = np.ones((3, 2))
print("ones_array:", ones_array)

# ✅ 특정 범위의 수 생성 (간격 기준)
range_array = np.arange(1, 10, 2)
print("range_array:", range_array)  # [1 3 5 7 9]

# ✅ 일정 간격으로 나누기 (개수 기준)
linspace_array = np.linspace(0, 10, 5)
print("linspace_array:", linspace_array)  # [ 0.   2.5  5.   7.5 10. ]

# ✅ 배열 형태 변경: reshape
array2 = np.array([1, 2, 3, 4, 5, 6])
reshape = np.reshape(array2, (2, 3))
print("reshape:", reshape)
# [[1 2 3]
#  [4 5 6]]

# ✅ 배열 크기 변경: resize (원소가 부족하면 반복)
resized = np.resize(array2, (3, 5))
print("resized:", resized)
# [[1 2 3 4 5]
#  [6 1 2 3 4]
#  [5 6 1 2 3]]

# ✅ 기본 사칙연산 (배열끼리)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("arr1 + arr2:", arr1 + arr2)
print("arr1 - arr2:", arr1 - arr2)
print("arr1 * arr2:", arr1 * arr2)
print("arr1 / arr2:", arr1 / arr2)

# ✅ 수학 함수 사용: 제곱근
arr1 = np.array([1, 4, 9, 16, 25])
sqrt_values = np.sqrt(arr1)
print("제곱근:", sqrt_values)  # [1. 2. 3. 4. 5.]

# ✅ 로그 함수
arr1 = np.array([1, 2.718, 10, 20])
log_values = np.log(arr1)
print("로그:", log_values)

# ✅ 삼각 함수
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
sin_values = np.sin(angles)
print("사인:", sin_values)
cos_values = np.cos(angles)
print("코사인:", cos_values)

# ✅ 배열 합치기
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.hstack((arr1, arr2))  # 수평 합치기 (1차원 기준으로 연결)
print("수평 합치기:", result)     # [1 2 3 4 5 6]

result = np.vstack((arr1, arr2))  # 수직 합치기 (2차원으로 아래로 쌓기)
print("수직 합치기:", result)
# [[1 2 3]
#  [4 5 6]]

result = np.column_stack((arr1, arr2))  # 열 기준 합치기 (세로로 짝지음)
print("열 기준 합치기:", result)
# [[1 4]
#  [2 5]
#  [3 6]]

# ✅ 배열 분할
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

result = np.hsplit(arr1, 3)  # 열을 기준으로 분할 (좌우 나눔)
print("수평 분할:", result)

result = np.vsplit(arr1, 2)  # 행을 기준으로 분할 (위아래 나눔)
print("수직 분할:", result)

# ✅ 브로드캐스팅 (스칼라 or 다른 차원과 자동 연산)
arr1 = np.array([1, 2, 3, 4])
scalar = 10
result = arr1 + scalar
print("스칼라 더하기:", result)  # [11 12 13 14]

# ✅ 브로드캐스팅: 1차원 + 2차원
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print("브로드캐스팅 (행별):", result)
# [[11 22 33]
#  [14 25 36]]

# ✅ 브로드캐스팅: 열 방향 더하기
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10], [20]])
result = arr1 + arr2
print("브로드캐스팅 (열별):", result)
# [[11 12 13]
#  [24 25 26]]


# ✅ 원본 팀 데이터: 팀명, 승, 패, 무, 승률
teams = [
    ["LG", 63, 55, 2, 0.534],
    ["SSG", 58, 62, 1, 0.483],
    ["KIA", 71, 48, 2, 0.597],
    ["NC", 52, 63, 2, 0.452],
    ["KT", 59, 61, 2, 0.492],
    ["롯데", 51, 61, 3, 0.455],
    ["두산", 62, 60, 0, 0.508],
    ["삼성", 66, 54, 2, 0.550],
    ["키움", 53, 67, 0, 0.442],
    ["한화", 56, 60, 2, 0.483],
]

# ✅ NumPy 배열로 변환 (dtype=object는 문자열+숫자 혼합을 허용)
np_team = np.array(teams, dtype=object)

# ✅ 승률 기준으로 내림차순 정렬
# np_team[:, 4] → 모든 행의 '승률' 열만 추출
# astype(float) → 문자열일 수도 있으므로 실수형으로 변환
# -np_team[:, 4] → 부호를 반대로 하여 내림차순 정렬
sorted_indices = np.argsort(-np_team[:, 4].astype(float))
print("sorted_indices: ", sorted_indices)

# ✅ 정렬된 인덱스를 이용하여 팀 정보 정렬
sorted_team = np_team[sorted_indices]
print("sorted_team: ", sorted_team)

# ✅ 정렬된 데이터를 텍스트 파일로 저장
file_path = "kbo_sorted.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write("============ 2024 한국 프로야구 성적표 ============\n\n")
    file.write("순위  팀    승   패  무   승률\n")

    # 각 팀 정보를 순위와 함께 출력
    for i, row in enumerate(sorted_team, 1):
        # 순위  팀이름   승  패  무  승률  → 각각 칸 맞추기
        file.write(
            f"{i:<5}{row[0]:<5}{row[1]:<4}{row[2]:<4}{row[3]:<4}{float(row[4]):.3f}\n")

# ✅ NumPy argsort 예제 (개념 설명용)
arr1 = np.array([3, 1, 4, 2, 5])

# argsort는 정렬 시 원래 인덱스의 순서를 반환
# [3, 1, 4, 2, 5] → 정렬하면 → [1, 2, 3, 4, 5]
# 정렬된 값들의 원래 위치는 → [1, 3, 0, 2, 4]
sorted_arr = np.argsort(arr1)
print("sorted_arr: ", sorted_arr)        # [1 3 0 2 4]
print("arr1: ", arr1[sorted_arr])        # [1 2 3 4 5]

scores = np.array([[85, 92, 78, 96], 
                   [88, 85, 90, 92], 
                   [90, 88, 85, 94]])
# 행: 학생 (김철수, 이영희, 박민수)
# 열: 과목 (국어, 수학, 영어, 과학)

print("1. 이영희의 모든 과목 점수:", scores[1])
print("2. 모든학생의 수학 점수:", scores[:, 1])
print("3. 90점 이상인 점수들만 선택:", scores[scores >= 90])
scores[0,2] = 95
print("4. 김철수의 영어 점수를 95점으로 수정",  scores[0])