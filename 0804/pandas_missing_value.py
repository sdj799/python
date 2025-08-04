# 결측값
import pandas as pd
import numpy as np

students = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운',None],
    '나이': [20, np.nan, 19, 22, 20,None],
    '수학': [85, 92, np.nan, 96, 83,None],
    '영어': [88, 85, 90, np.nan, 89,None],
    '전화번호': ['010-1234-5678', None, '010-9876-5432', '010-5555-1234', '',None]
})

print("=== 결측값이 있는 데이터 ===")
print(students)

print("=== 결측값 확인 ===")
print(students.isnull())

print("=== 열별 결측값 개수 확인 ===")
print(students.isnull().sum())

print("=== 전체 결측값 개수 확인 ===")
print(students.isnull().sum().sum())

print("=== 결측값 행 제거 ===")
print(students.dropna())

print("=== 특정 열의 결측값 제거 ===")
print(students.dropna(subset=['수학']))

print("=== 모든 값이 결측값인 행만 제거 ===")
print(students.dropna(how='all'))

print("=== 특정 값으로 결측값 채우기 ===")
print(students.fillna(0))
filled_custom = students.fillna({
    '나이':students['나이'].median(),
    '수학':students['수학'].mean(),
    '영어':students['영어'].mean(),
    '전화번호':'정보 없음',
})
print(filled_custom)

duplicate_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '김철수', '박민수', '이영희', '최지영'],
    '나이': [20, 21, 20, 19, 21, 22],
    '전공': ['컴퓨터', '수학', '컴퓨터', '물리', '수학', '화학']
})

print("=== 중복 데이터 ===")
print(duplicate_data)

print("=== 중복 확인 ===")
print(duplicate_data.duplicated())

print("=== 중복 개수 확인 ===")
print(duplicate_data.duplicated().sum())

print("=== 중복 제거 ===")
print(duplicate_data.drop_duplicates())

print("=== 특정 열 기준으로 중복 제거 ===")
print(duplicate_data.duplicated(subset='이름'))