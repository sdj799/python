# DataFrame
# 여러개의 Series가 합쳐진 2차원 표 형태의 데이터 구조
# 엑셀의 전체 시트와 같은 개념
# 행과 열을 가진 표 형태

import pandas as pd
# 딕셔너리로 생성
data = {
    "이름": ["철수", "영희", "민수", "지영"],
    "국어": [80,65,90,70],
    "수학": [92,95,63,80],
    "영어": [80,85,65,90]
}
df = pd.DataFrame(data)
print(df)

# 리스트의 리스트로 생성
data = [
    ["철수", 80,92,80],
    ["영희",65,95,85],
    ["민수",90,63,65],
    ["지영",70,80,90]
]

df = pd.DataFrame(data, columns=["이름", "국어", "수학", "영어"])
print(df)

# 각 열을 series로 만들어서 합치기
names = pd.Series(["철수", "영희", "민수", "지영"])
ko = pd.Series([80,65,90,70])
ma = pd.Series([92,95,63,80])
en = pd.Series([80,85,65,90])

df = pd.DataFrame({
    "이름":names,
    "국어":ko,
    "수학":ma,
    "영어":en
})
print(df)
# 빈 DataFrame 생성 후 열 추가
df = pd.DataFrame()
df["이름"]=["철수", "영희", "민수", "지영"]
df["국어"]=[80,65,90,70]
df["수학"]=[92,95,63,80]
df["영어"]=[80,85,65,90]
print(df)

print("=== DataFrame 주요 속성 ===")
print(f"모먕 (행, 열): {df.shape}")
print(f"전체 셀 개수: {df.size}")
print(f"열 이름들: {df.columns}")
print(f"인덱스: {df.index}")
print(f"데이터 타입들: {df.dtypes}")
print()
print(df.info())

print("=== DataFrame 데이터 미리보기 ===")
print("처음 2행:")
print(df.head(2))

print("마지막 2행:")
print(df.tail(2))

print(df.describe())

print("=== DataFrame 컬럼명 변경 ===")
df_eng = df.rename(columns={
    "이름": "name",
    "국어": "ko",
    "수학": "ma",
    "영어": "en"
})
print(df_eng)

df_indexed = df.set_index("이름")
print(df_indexed)

employee_data = {
    '이름': ['김대리', '박과장', '이부장', '최사원', '정대리'],
    '부서': ['개발팀', '영업팀', '기획팀', '개발팀', '인사팀'],
    '월급': [3500000, 5000000, 7000000, 2800000, 3200000],
    '입사년도': [2020, 2018, 2015, 2022, 2021],
    '나이': [28, 35, 40, 24, 30]
}

df_employee = pd.DataFrame(employee_data)
# 생성된 DataFrame 출력
print(df_employee)
# 전체 직원 수 출력
print("전체 직원수:", df_employee.shape[0])
# 전체 부서 수 출력
print("전체 부서수:", df_employee["부서"].nunique())
# 평균 월급 출력
print("평균 월급:", df_employee["월급"].mean())
# 평균 나이 출력
print("평균 나이:", df_employee["나이"].mean())

data = {
    "Name" : ["홍길동", "임꺽정", "성춘향"],
    "Age" : [25,30,35],
    "City":["Seoul", "Busan", "Incheon"]  
}

df = pd.DataFrame(data, index=["a","b","c"])
print("df.loc[b]", df.loc["b"])
print("df.loc[b, Age]", df.loc["b", "Age"])
print("df.loc[a:b, Age:City]", df.loc["a":"b", "Age":"City"])
print("df.loc[a, :]", df.loc["a", :])

print("df.iloc[1]", df.iloc[1])

print(df.iloc[:,1])

# 행 추가
new_row = {"Name": "이몽룡", "Age":30, "City":"포항"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df)

# 열 추가
df["직업"] = ["엔지니어", "의사", "디자이너", "개발자"]
print(df)

# 요소 수정
df.at[2,"City"] = "인천"
df.loc[df["Name"] == "임꺽정", "City"] = "부산"
print(df)

df.rename(columns={"Name":"이름","Age":"나이"}, inplace=True)
print(df)

students_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운', '홍길동', '신짱구'],
    '수학': [85, 92, 78, 96, 83, 89, 74],
    '영어': [88, 85, 90, 87, 89, 82, 76],
    '과학': [92, 88, 85, 90, 86, 91, 80],
    '학년': [2, 3, 1, 3, 2, 2, 1],
    '반': ['A', 'B', 'A', 'B', 'A', 'B', 'A']
})
# 전체 데이터 출력
print(students_data)
# 수학 점수만 선택해서 출력
print(students_data["수학"].tolist())
# 이름 수학 영어 열만 선택해서 출력
print(students_data.loc[:, "이름" :"영어"])
# 수학 점수가 90점 이상인 학생들을 출력
print(students_data[students_data["수학"] >= 90])
# 3학년 학생들만 출력
print(students_data[students_data["학년"] == 3])
# A반이면서 수학점수가 80점 이상인 학생들 출력
print(students_data[(students_data["수학"]>= 80) &  (students_data["반"] == "A")])

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
print(products.loc[[3,4]])
# loc를 사용해서 '상품명' '가격',  출력
print(products.loc[[3,4]])
# loc를 사용해서 첫 3행의 마지막 2열 출력
# loc를 사용해서 100000이상인 행의 '상품명'과 '브랜드' 출력
# 브랜드가 '로지텍'인 상품정보 출력