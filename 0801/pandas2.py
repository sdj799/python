# DataFrame
# 여러개의 Series가 합쳐진 2차원 표 형태의 데이터 구조
# 엑셀의 전체 시트와 같은 개념
# 행(row)과 열(column)을 가진 표 형태

import pandas as pd

print("=== DataFrame 생성 ===")

# 방법 1: 딕셔너리로 생성 (가장 일반적인 방법)
data = {
    "이름": ["철수", "영희", "민수", "지영"],    # 각 키가 열(column) 이름이 됨
    "국어": [80, 65, 90, 70],              # 각 값의 리스트가 열의 데이터가 됨
    "수학": [92, 95, 63, 80],
    "영어": [80, 85, 65, 90]
}

df = pd.DataFrame(data)  # 딕셔너리를 DataFrame으로 변환
print("1) 딕셔너리로 만든 DataFrame:")
print(df)
print()

# 추가: 딕셔너리의 키는 열 이름, 값의 리스트는 각 열의 데이터가 됩니다.
# 모든 리스트의 길이는 같아야 합니다.

# 방법 2: 리스트의 리스트로 생성
data = [
    ["철수", 80, 92, 80],    # 각 내부 리스트가 하나의 행(row)이 됨
    ["영희", 65, 95, 85],
    ["민수", 90, 63, 65],
    ["지영", 70, 80, 90]
]

df = pd.DataFrame(data, columns=["이름", "국어", "수학", "영어"])  # columns로 열 이름 지정
print("2) 리스트의 리스트로 만든 DataFrame:")
print(df)
print()

# 추가: 2차원 리스트를 사용할 때는 columns 매개변수로 열 이름을 별도로 지정해야 합니다.
# 각 내부 리스트는 하나의 행 데이터를 나타냅니다.

# 방법 3: Series들을 합쳐서 생성
names = pd.Series(["철수", "영희", "민수", "지영"])  # 이름 Series
ko = pd.Series([80, 65, 90, 70])                # 국어 점수 Series
ma = pd.Series([92, 95, 63, 80])                # 수학 점수 Series
en = pd.Series([80, 85, 65, 90])                # 영어 점수 Series

df = pd.DataFrame({
    "이름": names,    # 각 Series를 열로 지정
    "국어": ko,
    "수학": ma,
    "영어": en
})
print("3) Series들을 합쳐서 만든 DataFrame:")
print(df)
print()

# 추가: 이미 Series로 만들어진 데이터들을 DataFrame으로 합칠 때 유용합니다.
# 각 Series가 DataFrame의 한 열이 됩니다.

# 방법 4: 빈 DataFrame 생성 후 열 추가
df = pd.DataFrame()  # 빈 DataFrame 생성

df["이름"] = ["철수", "영희", "민수", "지영"]  # 열을 하나씩 추가
df["국어"] = [80, 65, 90, 70]
df["수학"] = [92, 95, 63, 80]
df["영어"] = [80, 85, 65, 90]
print("4) 빈 DataFrame에 열을 하나씩 추가:")
print(df)
print()

# 추가: 데이터를 점진적으로 추가할 때 유용합니다.
# df["새열이름"] = [데이터] 형태로 언제든 새 열을 추가할 수 있습니다.

print("=== DataFrame 주요 속성 ===")

print(f"모양 (행, 열): {df.shape}")           # (행의 개수, 열의 개수) 튜플 반환
print(f"전체 셀 개수: {df.size}")             # 전체 데이터 개수 = 행 × 열
print(f"열 이름들: {df.columns}")             # 모든 열 이름들의 목록
print(f"인덱스: {df.index}")                 # 행 인덱스들의 목록 (기본적으로 0, 1, 2, ...)
print(f"데이터 타입들:\n{df.dtypes}")          # 각 열의 데이터 타입
print()

# DataFrame의 전반적인 정보 확인
print("DataFrame 전체 정보:")
print(df.info())  # 열 개수, 데이터 타입, 메모리 사용량 등 종합 정보
print()

# 추가: shape는 (행, 열) 튜플을 반환하므로 df.shape[0]은 행 개수, df.shape[1]은 열 개수입니다.
# info()는 DataFrame의 구조를 한눈에 파악할 때 매우 유용합니다.

print("=== DataFrame 데이터 미리보기 ===")

print("처음 5행:")
print(df.head())      # 기본적으로 처음 5행을 보여줌
print()

print("처음 2행:")
print(df.head(2))     # 괄호 안 숫자만큼 처음 행들을 보여줌
print()

print("마지막 5행:")
print(df.tail())      # 기본적으로 마지막 5행을 보여줌
print()

print("마지막 2행:")
print(df.tail(2))     # 괄호 안 숫자만큼 마지막 행들을 보여줌
print()

# 숫자 데이터의 기본 통계 정보
print("숫자 열들의 기본 통계:")
print(df.describe())  # 개수, 평균, 표준편차, 최솟값, 25/50/75분위수, 최댓값
print()

# 추가: head()와 tail()은 큰 데이터셋에서 일부만 확인할 때 매우 유용합니다.
# describe()는 숫자 열에 대한 기본 통계를 제공하여 데이터 분포를 파악할 수 있습니다.

print("=== DataFrame 컬럼명 변경 ===")

# 열 이름 변경
df_eng = df.rename(columns={
    "이름": "name",      # 기존이름: 새이름 형태의 딕셔너리
    "국어": "ko",
    "수학": "ma",
    "영어": "en",
})
print("열 이름을 영어로 변경:")
print(df_eng)
print()

# 추가: rename() 함수는 원본 DataFrame을 변경하지 않고 새로운 DataFrame을 반환합니다.
# inplace=True 옵션을 추가하면 원본을 직접 변경할 수 있습니다.

# 특정 열을 인덱스로 설정
df_indexed = df.set_index('이름')  # '이름' 열을 행 인덱스로 설정
print("이름을 인덱스로 설정:")
print(df_indexed)
print()

# 추가: set_index()를 사용하면 특정 열을 행의 이름(인덱스)으로 만들 수 있습니다.
# 이렇게 하면 해당 열은 일반 열에서 사라지고 인덱스가 됩니다.

print("\n" + "="*50)
print("실습 예제 1: 상품 데이터")
print("="*50)

# 실습용 상품 데이터 생성
products = pd.DataFrame({
    '상품명': ['노트북', '마우스', '키보드', '모니터', '스피커'],
    '가격': [800000, 25000, 45000, 300000, 80000],
    '재고': [15, 50, 30, 8, 25],
    '카테고리': ['컴퓨터', '주변기기', '주변기기', '컴퓨터', '주변기기'],
    '평점': [4.5, 4.2, 4.0, 4.8, 3.9]
})

print("상품 정보:")
print(products)
print()

# DataFrame의 기본 분석
print(f"상품 수: {len(products)}개")                      # len()으로 행의 개수 확인
print(f"평균 가격: {products['가격'].mean():,.0f}원")        # 특정 열의 평균 계산
print(f"총 재고: {products['재고'].sum()}개")               # 특정 열의 합계 계산
print()

# 추가: DataFrame[열이름]으로 특정 열에 접근하면 Series가 반환됩니다.
# 따라서 Series의 모든 메서드(mean, sum, max 등)를 사용할 수 있습니다.

print("\n" + "="*50)
print("실습 예제 2: 직원 데이터")
print("="*50)

# 직원 데이터 생성
employee_data = {
    '이름': ['김대리', '박과장', '이부장', '최사원', '정대리'],
    '부서': ['개발팀', '영업팀', '기획팀', '개발팀', '인사팀'],
    '월급': [3500000, 5000000, 7000000, 2800000, 3200000],
    '입사년도': [2020, 2018, 2015, 2022, 2021],
    '나이': [28, 35, 40, 24, 30]
}

employee = pd.DataFrame(employee_data)

print("=== 직원 정보 ===")
print(employee)
print()

# 기본 통계 분석
print(f"전체 직원 수: {employee.shape[0]}명")                    # shape[0]는 행의 개수

# 고유값 개수 확인
# nunique()는 중복 제거 후 개수
print(f"전체 부서 수: {employee['부서'].nunique()}개")
# unique()는 중복 제거 후 실제 값들
print(f"부서 목록: {employee['부서'].unique()}")
print()

# 평균 계산
print(f"평균 월급: {employee['월급'].mean():,.0f}원")            # :,.0f는 천 단위 콤마 표시
print(f"평균 나이: {employee['나이'].mean():.1f}세")             # :.1f는 소수점 1자리까지
print()

# 추가: nunique()는 고유한 값의 개수를, unique()는 실제 고유값들을 반환합니다.
# :,.0f 같은 포매팅으로 숫자를 보기 좋게 표시할 수 있습니다.

print("\n" + "="*50)
print("DataFrame 인덱싱과 선택")
print("="*50)

# 예제 데이터 생성 (사용자 정의 인덱스 포함)
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, 30, 35],
    "City": ["Seoul", "Busan", "Incheon"]
}

df = pd.DataFrame(data, index=["a", "b", "c"])  # 인덱스를 a, b, c로 설정
print("예제 DataFrame:")
print(df)
print()

# .loc 사용법 (라벨 기반 인덱싱)
print("=== .loc 사용법 (라벨/이름 기반) ===")

print("1) 특정 행 선택 - df.loc['b']:")
print(df.loc["b"])      # 'b' 인덱스에 해당하는 행 전체 선택
print()

print("2) 특정 셀 선택 - df.loc['b', 'Age']:")
print(df.loc["b", "Age"])   # 'b' 행의 'Age' 열 값 선택
print()

print("3) 행과 열 범위 선택 - df.loc['a':'b', 'Age':'City']:")
print(df.loc["a":"b", "Age":"City"])    # 'a'부터 'b'행, 'Age'부터 'City'열 선택
print()

print("4) 모든 행, 특정 열들 - df.loc[:, 'Age':'City']:")
print(df.loc[:, "Age":"City"])          # 모든 행(:), 'Age'부터 'City'열 선택
print()

print("5) 특정 행, 모든 열 - df.loc['a', :]:")
print(df.loc["a", :])                   # 'a' 행, 모든 열(:) 선택
print()

# 추가: .loc는 라벨(이름) 기반 인덱싱입니다.
# df.loc[행, 열] 형태로 사용하며, :는 "모든 것"을 의미합니다.
# 범위 선택 시 끝점이 포함됩니다 ('a':'b'는 'a', 'b' 모두 포함).

print("=== .iloc 사용법 (위치 기반) ===")

print("1) 위치로 행 선택 - df.iloc[1]:")
print(df.iloc[1])           # 1번째 인덱스(두 번째) 행 선택
print()

print("2) 위치로 셀 선택 - df.iloc[1, 1]:")
print(df.iloc[1, 1])        # 1행 1열 위치의 값 선택
print()

print("3) 위치 범위로 선택 - df.iloc[0:2, 0:1]:")
print(df.iloc[0:2, 0:1])    # 0~1행, 0열 선택 (끝점 미포함)
print()

print("4) 특정 위치들 선택 - df.iloc[[1,2], [1,2]]:")
print(df.iloc[[1, 2], [1, 2]])  # 1,2번째 행과 1,2번째 열의 교집합
print()

print("5) 모든 행, 특정 열 - df.iloc[:, 1]:")
print(df.iloc[:, 1])        # 모든 행, 1번째 열
print()

print("6) 특정 행, 모든 열 - df.iloc[2, :]:")
print(df.iloc[2, :])        # 2번째 행, 모든 열
print()

# 추가: .iloc는 위치(정수) 기반 인덱싱입니다.
# 0부터 시작하는 정수 인덱스를 사용합니다.
# 범위 선택 시 끝점이 포함되지 않습니다 (0:2는 0, 1만 포함).

print("\n" + "="*50)
print("DataFrame 데이터 수정하기")
print("="*50)

# 행 추가
print("=== 행 추가 ===")
new_row = {"Name": "이몽룡", "Age": 30, "City": "포항"}        # 새로 추가할 행 데이터
df = pd.concat([df, pd.DataFrame([new_row])],
               ignore_index=True)  # 기존 DataFrame에 새 행 추가
print("새 행 추가 후:")
print(df)
print()

# 추가: pd.concat()으로 DataFrame들을 합칠 수 있습니다.
# ignore_index=True는 인덱스를 0, 1, 2, ... 순서로 새로 매깁니다.
# new_row를 DataFrame으로 변환할 때 [new_row]처럼 리스트로 감싸야 합니다.

# 열 추가
print("=== 열 추가 ===")
df["직업"] = ["엔지니어", "의사", "디자이너", "개발자"]  # 새로운 열을 간단히 추가
print("새 열 추가 후:")
print(df)
print()

# 추가: df["새열이름"] = [데이터] 형태로 쉽게 새 열을 추가할 수 있습니다.
# 데이터의 개수는 기존 행 개수와 일치해야 합니다.

# 특정 위치의 값 수정
print("=== 데이터 값 수정 ===")
df.at[2, "City"] = '인천'    # 2번째 행의 'City' 열 값을 '인천'으로 변경
print("2번째 행의 City를 '인천'으로 변경:")
print(df)
print()

# 조건을 만족하는 행의 값 수정
df.loc[df["Name"] == "임꺽정", "City"] = "부산"  # 이름이 '임꺽정'인 행의 City를 '부산'으로 변경
print("임꺽정의 City를 '부산'으로 변경:")
print(df)
print()

# 추가: .at[행, 열]은 특정 위치의 값을 수정할 때 사용합니다.
# 조건부 수정은 df.loc[조건, 열] = 새값 형태로 사용합니다.

# 열 이름 변경 (inplace 사용)
print("=== 열 이름 변경 ===")
df.rename(columns={"Name": "이름", "Age": "나이"},
          inplace=True)  # inplace=True로 원본 직접 수정
print("열 이름을 한글로 변경:")
print(df)
print()

# 추가: inplace=True를 사용하면 새로운 DataFrame을 만들지 않고 원본을 직접 수정합니다.
# inplace=False(기본값)일 때는 수정된 새 DataFrame을 반환합니다.

print("\n" + "="*50)
print("핵심 정리")
print("="*50)
print("""
DataFrame의 주요 개념과 활용법:

1. DataFrame 생성:
   - 딕셔너리: pd.DataFrame({열이름: [데이터]})
   - 2차원 리스트: pd.DataFrame(data, columns=[열이름들])
   - Series 결합: pd.DataFrame({열이름: Series})

2. 데이터 접근:
   - 열 선택: df['열이름'] 또는 df[['열1', '열2']]
   - .loc[행, 열]: 라벨 기반 (이름으로 접근)
   - .iloc[행, 열]: 위치 기반 (숫자로 접근)

3. 유용한 속성과 메서드:
   - 구조 확인: .shape, .info(), .head(), .tail()  
   - 통계: .describe(), .mean(), .sum() 등
   - 고유값: .unique(), .nunique()

4. 데이터 수정:
   - 행 추가: pd.concat()
   - 열 추가: df['새열'] = [데이터]
   - 값 수정: .at[행, 열] = 새값
   - 조건부 수정: df.loc[조건, 열] = 새값

DataFrame은 실제 데이터 분석에서 가장 많이 사용하는 구조입니다.
엑셀과 비슷하지만 더 강력한 기능을 제공합니다!
""")

students_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운', '홍길동', '신짱구'],
    '수학': [85, 92, 78, 96, 83, 89, 74],
    '영어': [88, 85, 90, 87, 89, 82, 76],
    '과학': [92, 88, 85, 90, 86, 91, 80],
    '학년': [2, 3, 1, 3, 2, 2, 1],
    '반': ['A', 'B', 'A', 'B', 'A', 'B', 'A']
})

# 1. 전체 데이터 출력
print("=== 전체 데이터 ===")
print(students_data)
print()

# 2. 수학 점수만 선택
print("=== 수학 점수 ===")
print(students_data["수학"])
print()

# 3. 이름, 수학, 영어, 열만 선택
print("=== 이름, 수학, 영어 ===")
print(students_data[["이름", "수학", "영어"]])
print()

# 4. 수학 90점 이상
print("=== 수학 90점 이상 ===")
high_math = students_data[students_data["수학"] >= 90]
print(high_math[["이름", "수학"]])
print()

# 5. 3학년 학생들
print("=== 3학년 학생들 ===")
grade3 = students_data[students_data["학년"] == 3]
print(grade3[["이름", "학년", "반"]])
print()

# 6. A반 이면서 수학 80점 이상
print("=== A반 이면서 수학 80점 이상 ===")
a_class = students_data[((students_data["반"] == "A") &
                        (students_data["수학"] >= 80))]
print(a_class[["이름", "반", "수학"]])
print()
products = pd.DataFrame({
    '상품코드': ['A001', 'A002', 'B001', 'B002', 'C001'],
    '상품명': ['노트북', '태블릿', '마우스', '키보드', '모니터'],
    '가격': [1200000, 800000, 30000, 60000, 400000],
    '재고': [20, 15, 100, 80, 25],
    '브랜드': ['삼성', 'LG', '로지텍', '로지텍', '삼성']
})

print(products)
# loc를 사용해서 첫번째와 세번째행 출력
print(products.loc[[0,2]])
# loc를 사용해서 마지막 두행 출력
print(products.iloc[-2:])
# loc를 사용해서 '상품명' '가격',  출력
print(products.loc[: , "상품명": "가격"])
# loc를 사용해서 첫 3행의 마지막 2열 출력
print(products.iloc[:3, -2: ])
# loc를 사용해서 100000이상인 행의 '상품명'과 '브랜드' 출력
print(products.loc[products["가격"] >= 100000, ["상품명", "브랜드"]])
# 브랜드가 '로지텍'인 상품정보 출력
print(products.loc[products["브랜드"] == "로지텍"])