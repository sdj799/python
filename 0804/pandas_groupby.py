# groupby
# 데이터를 특정 기준을 그룹으로 나누어 집계하는 기능

import pandas as pd

students = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수', '최지영', '정다운', '홍길동'],
    '학년': [2, 3, 1, 3, 2, 1],
    '반': ['A', 'B', 'A', 'B', 'A', 'B'],
    '수학': [85, 92, 78, 96, 83, 88],
    '영어': [88, 85, 90, 87, 89, 82],
    '과학': [92, 88, 85, 90, 86, 91]
})

print("=== 원본 데이터 ===")
print(students)

grade_groups = students.groupby('학년')
print("그룹 개수: " , grade_groups.ngroups)
print("그룹 키 들: " , grade_groups.groups.keys())

print("=== 집계 함수 ===")
grade_mean = students.groupby('학년')[['수학', '영어', '과학']].mean()
print(grade_mean)

grade_max = students.groupby('학년')[['수학', '영어', '과학']].max()
print(grade_max)

grade_size = students.groupby('학년').size()
print(grade_size)

math_stats = students.groupby('반')['수학'].agg([
    'count', 'mean', 'median', 'std', 'min', 'max'
])
print(math_stats)

# 사용자 정의 함수
def score_range(scores):
    return scores.max() - scores.min()

range_stats = students.groupby('학년')['수학'].agg([
    ('평균', 'mean'),
    ('범위', score_range),
    ('학생수', 'count')
])

print(range_stats)

print("=== 여러열에 대한 집계함수 ===")
multi_agg = students.groupby('반').agg({
    '수학' : ['mean','max'],
    '영어': ['count','min'],
    '과학': 'std'
})
print(multi_agg)

# 피봇 테이블
# 복잡한 데이터를 요약, 집계, 분석 할 수 있도록 도와주는 도구
# 데이터의 행과 열을 기준으로 그룹응ㄹ 나눈 뒤
# 그룹별로 합계, 평균, 개수 등 요약된 값을 보여주는 표

pivot_basic = students.pivot_table(
    values=['수학','영어','과학'],
    index='학년',
    columns='반',
    aggfunc='mean'
)
print(pivot_basic)

employees = pd.DataFrame({
    '이름': ['김대리', '박과장', '이부장', '최사원', '정대리', '한과장', '송사원', '조대리'],
    '부서': ['개발', '영업', '기획', '개발', '인사', '영업', '개발', '기획'],
    '직급': ['대리', '과장', '부장', '사원', '대리', '과장', '사원', '대리'],
    '연봉': [4500, 6000, 8000, 3200, 4200, 5800, 3500, 4800],
    '경력': [3, 8, 15, 1, 5, 7, 2, 6],
    '성별': ['남', '남', '여', '남', '여', '여', '남', '남']
})

# 부서별 평균 연봉을 계산하세요
print(employees.groupby('부서')['연봉'].mean())
# 직급별 직원 수를 계산하세요
print(employees.groupby('직급').size())
# 부서별 연봉의 최댓값, 최솟값, 평균을 구하세요
print(employees.groupby('부서')['연봉'].agg([
    ('최대값', 'max'),
    ('최솟값', 'min'),
    ('평균', 'mean')
]))
# 성별로 그룹화하여 평균 연봉과 평균 경력을 계산하세요
print(employees.groupby('성별')[['연봉', '경력']].mean())
# 부서와 직급으로 그룹화하여 평균연봉을 구하세요
print(employees.groupby(['부서', '직급'])['연봉'].mean())