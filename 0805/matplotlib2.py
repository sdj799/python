# Matplotlib 막대 그래프 강의 자료
# 카테고리별 데이터를 시각적으로 비교하는 가장 효과적인 방법

import matplotlib.pyplot as plt  # 그래프 그리기 위한 pyplot 모듈
import numpy as np               # 수치 계산을 위한 NumPy

# ============================================================================
# 1. 한글 폰트 설정 (한글 깨짐 방지)
# ============================================================================
plt.rcParams['font.family'] = ['DejaVu Sans', 'Malgun Gothic']  # 폰트 우선순위 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# ============================================================================
# 2. 샘플 데이터 준비
# ============================================================================
categories = ['A', 'B', 'C', 'D', 'E']    # 카테고리 (x축에 표시될 항목들)
values = [23, 52, 34, 42, 31]             # 각 카테고리의 값 (막대의 높이)

print("=== 막대 그래프 데이터 ===")
print(f"카테고리: {categories}")
print(f"값: {values}")
print()

# 💡 막대 그래프 사용 시기:
# - 카테고리별 데이터 비교 (예: 지역별 매출, 제품별 판매량)
# - 순위나 크기 비교가 중요한 경우
# - 이산적(discrete) 데이터 표현

# 큰 그래프 창 생성 (2행 3열 레이아웃)
plt.figure(figsize=(15, 10))

# ============================================================================
# 3-1. 기본 막대 그래프 (첫 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 1)

# 기본 막대 그래프 생성
bars = plt.bar(categories,          # x축 카테고리
               values,              # y축 값 (막대 높이)
               color="skyblue",     # 막대 색상
               linewidth=2)         # 막대 테두리 선 두께

plt.title('기본 막대 그래프')        # 그래프 제목
plt.ylabel('판매량')               # y축 라벨

# 막대 위에 값 표시하기
for i, val in enumerate(values):   # enumerate: 인덱스와 값을 동시에 가져옴
    plt.text(i,                    # x 좌표 (카테고리 인덱스)
             val + 1,              # y 좌표 (값 + 여백)
             str(val),             # 표시할 텍스트
             ha='center',          # 수평 정렬 (center, left, right)
             va='top')             # 수직 정렬 (top, bottom, center)

# 💡 plt.text() 매개변수 설명:
# - ha (horizontal alignment): 'center', 'left', 'right'
# - va (vertical alignment): 'top', 'bottom', 'center'
# - 막대 위에 정확한 값을 표시하여 가독성 향상

plt.grid(True, alpha=0.5)          # 격자 표시 (투명도 50%)

# ============================================================================
# 3-2. 수평 막대 그래프 (두 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 2)

# 수평 막대 그래프 생성 (barh = bar horizontal)
bars = plt.barh(categories,         # y축 카테고리 (수평이므로 y축에 카테고리 표시)
                values,             # x축 값 (막대 길이)
                color="skyblue",    # 막대 색상
                linewidth=2)        # 막대 테두리 선 두께

plt.title('수평 막대 그래프')        # 그래프 제목
plt.xlabel('판매량')               # x축 라벨 (수평 막대에서는 x축이 값)

# 💡 수평 막대 그래프 (barh) 사용 시기:
# - 카테고리 이름이 길어서 세로로 표시하기 어려운 경우
# - 많은 카테고리가 있어 가로 공간이 부족한 경우
# - 값의 비교보다는 순위가 중요한 경우

# ============================================================================
# 3-3. 다양한 색상의 막대 그래프 (세 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 3)

# 컬러맵을 사용한 그라데이션 색상 생성
colors = plt.cm.viridis(np.linspace(0, 1, len(categories)))
# plt.cm.viridis: viridis 컬러맵 (보라→파랑→초록→노랑)
# np.linspace(0, 1, len(categories)): 0~1 사이를 카테고리 수만큼 균등 분할

bars = plt.bar(categories, values,
               color=colors,        # 각 막대마다 다른 색상 적용
               linewidth=2)

plt.title('다채로운 색상 막대 그래프')
plt.ylabel('판매량')

# 💡 matplotlib 컬러맵 종류:
# - viridis, plasma, inferno, magma (인지적으로 균등한 색상)
# - coolwarm, RdYlBu (발산형 색상)
# - Reds, Blues, Greens (단일 색상 계열)

# ============================================================================
# 3-4. 정렬된 막대 그래프 (네 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 4)

# 값 기준으로 내림차순 정렬
sorted_indices = np.argsort(values)[::-1]  # argsort(): 정렬된 인덱스 반환, [::-1]: 역순
sorted_categories = [categories[i] for i in sorted_indices]  # 정렬된 순서로 카테고리 재배치
sorted_values = [values[i] for i in sorted_indices]          # 정렬된 순서로 값 재배치

# 💡 np.argsort() 설명:
# - 배열을 정렬했을 때의 인덱스를 반환
# - [::-1]을 사용하여 내림차순으로 변경
# - 원본 데이터와 카테고리의 대응 관계를 유지하면서 정렬 가능

bars = plt.bar(sorted_categories, sorted_values, color="skyblue")

plt.title('값 기준 정렬 막대 그래프 (내림차순)')
plt.ylabel('판매량')
plt.xticks(rotation=45)            # x축 라벨을 45도 회전 (긴 라벨 처리용)

# 💡 정렬의 장점:
# - 데이터 비교가 쉬워짐
# - 최고값, 최저값을 한눈에 파악 가능
# - 패턴과 트렌드 발견이 용이

# ============================================================================
# 3-5. 막대 그래프 스타일링 고급 기법 (다섯 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 5)

# 막대 그래프에 그라데이션과 테두리 효과 적용
bars = plt.bar(categories, values,
               color='lightcoral',     # 기본 색상
               edgecolor='darkred',    # 테두리 색상
               linewidth=2,            # 테두리 두께
               alpha=0.8)              # 투명도 (0=투명, 1=불투명)

# 각 막대 위에 값과 백분율 동시 표시
total = sum(values)  # 전체 합계 계산
for i, val in enumerate(values):
    percentage = (val / total) * 100  # 백분율 계산
    plt.text(i, val + 1,
             f'{val}\n({percentage:.1f}%)',  # 값과 백분율을 줄바꿈으로 구분
             ha='center', va='bottom',
             fontsize=9)                     # 글자 크기 조정

plt.title('고급 스타일링 막대 그래프')
plt.ylabel('판매량')

# 💡 고급 스타일링 요소:
# - edgecolor: 막대 테두리 색상
# - alpha: 투명도 조절로 시각적 깊이감 연출
# - 백분율 표시로 전체 대비 비율 정보 제공

# ============================================================================
# 3-6. 그룹별 막대 그래프 (여섯 번째 서브플롯)
# ============================================================================
plt.subplot(2, 3, 6)

# 두 그룹 데이터 준비 (예: 2020년, 2021년 비교)
values_2020 = [20, 45, 30, 35, 25]
values_2021 = [25, 55, 40, 50, 35]

x = np.arange(len(categories))    # 카테고리 위치를 숫자로 변환 [0, 1, 2, 3, 4]
width = 0.35                      # 막대 너비

# 두 개의 막대를 나란히 배치
bars1 = plt.bar(x - width/2, values_2020,  # 첫 번째 그룹 (왼쪽)
                width, label='2020년', color='lightblue')
bars2 = plt.bar(x + width/2, values_2021,  # 두 번째 그룹 (오른쪽)
                width, label='2021년', color='orange')

plt.title('연도별 비교 막대 그래프')
plt.ylabel('판매량')
plt.xlabel('제품 카테고리')
plt.xticks(x, categories)         # x축 눈금 위치와 라벨 설정
plt.legend()                      # 범례 표시

# 💡 그룹별 막대 그래프 핵심:
# - x 위치를 width만큼 좌우로 이동시켜 막대를 나란히 배치
# - np.arange()로 카테고리 위치를 숫자화
# - plt.xticks()로 원래 카테고리 이름 복원

# 모든 서브플롯의 레이아웃 자동 조정
plt.tight_layout()
plt.show()

# ============================================================================
# 4. 막대 그래프 실전 예제
# ============================================================================
print("\n=== 실전 예제: 월별 매출 분석 ===")

# 실제 비즈니스 데이터 시뮬레이션
months = ['1월', '2월', '3월', '4월', '5월', '6월']
sales = [150, 180, 220, 195, 240, 280]

plt.figure(figsize=(10, 6))

# 색상을 매출 크기에 따라 동적으로 설정
colors = ['red' if x < 200 else 'orange' if x <
          250 else 'green' for x in sales]

bars = plt.bar(months, sales, color=colors, alpha=0.7, edgecolor='black')

# 평균선 추가
avg_sales = np.mean(sales)
plt.axhline(y=avg_sales, color='blue', linestyle='--',
            label=f'평균: {avg_sales:.1f}만원')

# 막대 위에 값 표시
for bar, sale in zip(bars, sales):
    plt.text(bar.get_x() + bar.get_width()/2, sale + 5,
             f'{sale}만원', ha='center', va='bottom', fontweight='bold')

plt.title('2024년 상반기 월별 매출 현황', fontsize=16, fontweight='bold')
plt.ylabel('매출 (만원)', fontsize=12)
plt.xlabel('월', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')  # y축에만 격자 표시

# 💡 실전 팁:
# - 조건부 색상으로 임계값 기준 시각화
# - 평균선으로 기준점 제공
# - 폰트 굵기와 크기로 중요 정보 강조

plt.show()

# ============================================================================
# 5. 학습 요약
# ============================================================================
print("\n=== 막대 그래프 학습 요약 ===")
print("1. plt.bar(): 세로 막대 그래프")
print("2. plt.barh(): 가로 막대 그래프")
print("3. color, edgecolor, alpha: 색상과 투명도 설정")
print("4. plt.text(): 막대 위에 값 표시")
print("5. np.argsort(): 데이터 정렬을 위한 인덱스 생성")
print("6. 그룹별 비교: 막대 위치 조정으로 나란히 배치")
print("7. plt.axhline(): 평균선이나 기준선 추가")
print("8. 컬러맵 활용: 시각적 매력도 향상")
print("9. 조건부 색상: 데이터 특성에 따른 색상 구분")
print("10. 실전 활용: 비즈니스 데이터 분석과 시각화")