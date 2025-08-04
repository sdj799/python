import pandas as pd

students = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운'],
    '수학': [85, 92, 78, 96, 83],
    '영어': [88, 85, 90, 87, 89],
    '나이': [20, 21, 19, 22, 20]
})

math_asc = students.sort_values('수학')
print("수학 점수 오름차순:")
print(math_asc)

math_desc = students.sort_values('수학', ascending=False)
print('수학 점수 내림차순:')
print(math_desc)

# 나이 정렬 후 수학 정렬
multi_asc = students.sort_values(['나이','수학'])
print("나이, 수학 오름차순:")
print(multi_asc)

multi_desc = students.sort_values(['나이', '수학'], ascending=[True, False])
print('나이 오름차순 수학 내림차순:')
print(multi_desc)

index_sort = students.sort_index()
print('인덱스 기준 정렬:')
print(index_sort)

column_sort = students.sort_index(axis=1)
print('컬럼명 기준 정렬:')
print(column_sort)

students_indexed = students.set_index('이름')
print("이름을 인덱스로 설정:")
print(students_indexed)

print("원본: ")
print(students)

students.set_index("이름", inplace=True)
print("원본 변경: ")
print(students)

students_reset = students.reset_index()
print("인덱스를 열로 복원: ")
print(students_reset)

kim_info = students.loc["김철수"]
print("철수 정보")
print(kim_info)

sales_data = pd.DataFrame({
    '지역': ['서울', '서울', '부산', '부산', '서울', '부산'],
    '분기': ['Q1', 'Q2', 'Q1', 'Q2', 'Q3', 'Q3'],
    '매출': [100, 120, 80, 90, 110, 95],
    '직원수': [10, 12, 8, 9, 11, 8]
})

print("=== 다중 인덱스 ===")
multi_indexed = sales_data.set_index(['지역', '분기'])
print(multi_indexed)

seoul_q1 = multi_indexed.loc[('서울', 'Q1')]
print(seoul_q1)

seoul_all = multi_indexed.loc['서울']
print(seoul_all)

students_scores = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운', '홍길동'],
    '수학': [85, 92, 78, 96, 83, 88],
    '영어': [88, 85, 90, 87, 89, 82],
    '과학': [92, 88, 85, 90, 86, 91],
    '학년': [2, 3, 1, 3, 2, 1],
    '반': ['A', 'B', 'A', 'B', 'A', 'B']
})

# 1. 수학 점수 기준으로 내림차순 정렬하세요
print(students_scores.sort_values("수학", ascending=False))
# 2. 학년을 먼저, 그 다음 수학 점수로 오름차순 정렬하세요
print(students_scores.sort_values(["학년", "수학"]))
# 3. 학년은 오름차순, 수학 점수는 내림차순으로 정렬하세요
print(students_scores.sort_values(["학년", "수학"], ascending=[True,False]))
# 4. 총점을 계산하여 새로운 열에 추가하고, 총점 기준으로 내림차순 정렬하세요
students_scores["총점"] = students_scores[["수학", "영어", "과학"]].sum(axis=1)
print(students_scores.sort_values("총점", ascending=False))
# 5. 영어 점수가 가장 높은 학생 3명을 찾으세요
print(students_scores.sort_values("영어", ascending=False).head(3))