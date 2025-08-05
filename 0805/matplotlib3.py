# Matplotlib 산점도(Scatter Plot) 강의 자료
# 두 변수 간의 상관관계를 시각적으로 분석하는 최적의 도구

import matplotlib.pyplot as plt  # 그래프 그리기 위한 pyplot 모듈
import numpy as np               # 수치 계산과 랜덤 데이터 생성을 위한 NumPy

# ============================================================================
# 1. 한글 폰트 설정 (한글 깨짐 방지)
# ============================================================================
plt.rcParams['font.family'] = ['DejaVu Sans', 'Malgun Gothic']  # 폰트 우선순위 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# ============================================================================
# 2. 산점도란 무엇인가?
# ============================================================================
print("=== 산점도(Scatter Plot) 개념 ===")
print("• 두 연속형 변수 간의 관계를 점으로 표현하는 그래프")
print("• 상관관계, 패턴, 이상치(outlier) 발견에 유용")
print("• 예: 키와 몸무게, 공부시간과 성적, 광고비와 매출 등")
print()

# 💡 산점도 사용 시기:
# - 두 변수 간의 상관관계 분석
# - 데이터의 분포 패턴 파악
# - 이상치(outlier) 발견
# - 군집(cluster) 분석

# ============================================================================
# 3. 첫 번째 예제: 고객 분석 데이터
# ============================================================================
print("=== 첫 번째 예제: 고객 나이 vs 구매액 분석 ===")

# 재현 가능한 랜덤 데이터를 위한 시드 설정
np.random.seed(42)  # 시드를 고정하면 항상 같은 랜덤 데이터 생성

# 샘플 데이터 생성 (100명의 고객 데이터)
customer_age = np.random.randint(15, 70, 100)  # 15~70세 사이의 랜덤 나이 100개

# 💡 상관관계가 있는 데이터 생성 기법:
# 나이에 비례하는 수입 + 랜덤 노이즈 = 현실적인 데이터
customer_income = customer_age * 0.8 + np.random.normal(0, 10, 100)
# customer_age * 0.8: 나이와 비례하는 기본 수입
# np.random.normal(0, 10, 100): 평균 0, 표준편차 10인 정규분포 노이즈

# 수입에 비례하는 구매액 생성
purchase_amount = customer_income * 0.3 + np.random.normal(0, 5, 100)
# customer_income * 0.3: 수입의 30%를 구매에 사용
# np.random.normal(0, 5, 100): 개인차를 나타내는 노이즈

# 성별 데이터 생성 (범주형 변수)
gender = np.random.choice(['남성', '여성'], 100)  # 100개의 랜덤 성별 데이터

print(f"생성된 데이터 샘플:")
print(f"나이: {customer_age[:5]}")          # 처음 5개 데이터 출력
print(f"수입: {customer_income[:5]:.1f}")   # 소수점 1자리까지 출력
print(f"구매액: {purchase_amount[:5]:.1f}")
print(f"성별: {gender[:5]}")
print()

# ============================================================================
# 4. 성별에 따른 산점도 그리기
# ============================================================================
plt.figure(figsize=(12, 8))  # 그래프 크기 설정

print("=== 성별에 따른 색상과 마커 구분 ===")

# 성별에 따라 다른 색상과 마커로 구분하여 그리기
for g, color, marker in [('남성', 'blue', 'o'), ('여성', 'red', 's')]:
    # 💡 튜플 언패킹: 한 번에 여러 변수에 값 할당
    # g = '남성' 또는 '여성'
    # color = 'blue' 또는 'red'
    # marker = 'o'(원) 또는 's'(사각형)

    # 불리언 마스킹으로 특정 성별 데이터만 선택
    mask = gender == g  # True/False 배열 생성
    # 예: ['남성', '남성', '여성'] == '남성' → [True, True, False]

    print(f"{g} 고객 수: {np.sum(mask)}명")  # True의 개수 = 해당 성별 고객 수

    # 마스킹된 데이터로 산점도 그리기
    plt.scatter(customer_age[mask],      # 해당 성별의 나이 데이터만 선택
                purchase_amount[mask],   # 해당 성별의 구매액 데이터만 선택
                c=color,                 # 점의 색상
                marker=marker,           # 점의 모양
                s=60,                    # 점의 크기 (size)
                alpha=0.7,               # 투명도 (0=투명, 1=불투명)
                label=f'{g} 고객',       # 범례에 표시될 라벨
                linewidth=0.5)           # 점 테두리 선 두께

# 💡 불리언 마스킹 (Boolean Masking):
# - 조건에 맞는 데이터만 선택하는 NumPy의 강력한 기능
# - mask = gender == '남성' → [True, False, True, ...]
# - customer_age[mask] → True인 위치의 데이터만 추출

plt.title('고객 나이 vs 구매액 분석', fontsize=16, fontweight='bold')
plt.xlabel('나이 (세)', fontsize=12)
plt.ylabel('구매액 (만원)', fontsize=12)
plt.legend(fontsize=11)              # 범례 표시
plt.grid(True, alpha=0.5)            # 격자 표시

plt.tight_layout()
plt.show()

# ============================================================================
# 5. 두 번째 예제: 카페 지점별 성과 분석 (3차원 데이터)
# ============================================================================
print("\n=== 두 번째 예제: 카페 지점별 성과 분석 ===")

# 새로운 랜덤 시드로 다른 데이터 생성
np.random.seed(42)

# 실제 서울 지역명으로 카페 지점 데이터 생성
locations = ['강남', '홍대', '명동', '신촌', '이태원',
             '잠실', '건대', '신림', '종로', '마포']

# 각 지점의 성과 데이터 생성
daily_customers = np.random.randint(100, 500, 10)      # 일일 고객 수 (100~500명)
avg_spending = np.random.uniform(8000, 15000, 10)      # 평균 지출액 (8,000~15,000원)
store_size = np.random.uniform(20, 80, 10)             # 매장 크기 (20~80평)

# 💡 다양한 랜덤 함수:
# - randint(low, high, size): 정수 범위의 랜덤값
# - uniform(low, high, size): 실수 범위의 균등분포 랜덤값
# - normal(mean, std, size): 정규분포 랜덤값

print("생성된 카페 데이터 샘플:")
for i in range(3):  # 처음 3개 지점만 출력
    print(f"{locations[i]}: 고객 {daily_customers[i]}명, "
          f"평균지출 {avg_spending[i]:.0f}원, 크기 {store_size[i]:.1f}평")
print()

# 지역별 고유 색상 매핑 (딕셔너리 활용)
location_colors = {
    '강남': 'gold',      # 황금색 (고급스러운 이미지)
    '홍대': 'purple',    # 보라색 (젊고 활기찬 이미지)
    '명동': 'red',       # 빨간색 (쇼핑의 중심)
    '신촌': 'blue',      # 파란색 (대학가)
    '이태원': 'green',   # 초록색 (국제적인 이미지)
    '잠실': 'orange',    # 주황색 (가족 단위)
    '건대': 'pink',      # 핑크색 (젊은 층)
    '신림': 'brown',     # 갈색 (학생가)
    '종로': 'gray',      # 회색 (전통과 현대)
    '마포': 'cyan'       # 청록색 (문화의 거리)
}

# 💡 딕셔너리를 활용한 색상 매핑:
# - 각 카테고리별로 고유한 색상 지정
# - 코드의 가독성과 유지보수성 향상
# - 색상에 의미를 부여하여 직관적 이해 도움

plt.figure(figsize=(12, 8))

# ============================================================================
# 6. 3차원 정보를 2차원 산점도로 표현하기
# ============================================================================
print("=== 3차원 데이터의 2차원 산점도 표현 ===")
print("X축: 일일 고객 수")
print("Y축: 평균 지출액")
print("점 크기: 매장 크기")
print("점 색상: 지역별 구분")
print()

# 각 지점별로 개별 산점도 그리기
for i, location in enumerate(locations):
    plt.scatter(daily_customers[i],           # x축: 일일 고객 수
                avg_spending[i],              # y축: 평균 지출액
                c=location_colors[location],  # 색상: 지역별 고유 색상
                s=store_size[i] * 20,         # 크기: 매장 크기에 비례 (20배 확대)
                alpha=0.7,                    # 투명도
                linewidth=2,                  # 테두리 선 두께
                edgecolor='black',            # 테두리 색상 (명시적으로 추가)
                label=location)               # 범례 라벨

# 💡 산점도에서 3차원 정보 표현 방법:
# - X, Y축: 두 주요 변수
# - 점 크기: 세 번째 변수 (연속형)
# - 점 색상: 네 번째 변수 (범주형)
# - 이렇게 하면 4차원 정보까지 2차원 그래프에 표현 가능!

plt.title('카페 지점별 성과 분석 (크기 = 매장면적)', fontsize=16, fontweight='bold')
plt.xlabel('일일 고객 수 (명)', fontsize=12)
plt.ylabel('평균 지출액 (원)', fontsize=12)
plt.grid(True, alpha=0.5)

# 범례를 그래프 외부에 배치 (그래프가 가려지지 않도록)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()

# ============================================================================
# 7. 산점도 고급 활용 예제
# ============================================================================
print("\n=== 고급 산점도 활용 예제 ===")

# 더 복잡한 데이터 패턴 생성
np.random.seed(123)  # 다른 시드로 새로운 패턴

# 상관관계가 다양한 데이터셋 생성
n_points = 200

# 강한 양의 상관관계 데이터
x1 = np.random.normal(50, 15, n_points)
y1 = x1 * 0.8 + np.random.normal(0, 5, n_points)

# 강한 음의 상관관계 데이터
x2 = np.random.normal(30, 10, n_points)
y2 = -x2 * 0.6 + 100 + np.random.normal(0, 8, n_points)

# 상관관계가 없는 데이터
x3 = np.random.normal(40, 12, n_points)
y3 = np.random.normal(60, 20, n_points)

plt.figure(figsize=(15, 5))

# 💡 다양한 상관관계 패턴:
# 1. 양의 상관관계: 한 변수가 증가하면 다른 변수도 증가
# 2. 음의 상관관계: 한 변수가 증가하면 다른 변수는 감소
# 3. 무상관: 두 변수 간에 뚜렷한 관계가 없음

# 7-1. 강한 양의 상관관계
plt.subplot(1, 3, 1)
plt.scatter(x1, y1, alpha=0.6, color='blue', s=30)
plt.title('강한 양의 상관관계\n(r ≈ 0.8)', fontsize=12, fontweight='bold')
plt.xlabel('X 변수')
plt.ylabel('Y 변수')
plt.grid(True, alpha=0.3)

# 7-2. 강한 음의 상관관계
plt.subplot(1, 3, 2)
plt.scatter(x2, y2, alpha=0.6, color='red', s=30)
plt.title('강한 음의 상관관계\n(r ≈ -0.6)', fontsize=12, fontweight='bold')
plt.xlabel('X 변수')
plt.ylabel('Y 변수')
plt.grid(True, alpha=0.3)

# 7-3. 상관관계 없음
plt.subplot(1, 3, 3)
plt.scatter(x3, y3, alpha=0.6, color='green', s=30)
plt.title('상관관계 없음\n(r ≈ 0)', fontsize=12, fontweight='bold')
plt.xlabel('X 변수')
plt.ylabel('Y 변수')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# 8. 실전 비즈니스 분석 예제
# ============================================================================
print("\n=== 실전 예제: 온라인 쇼핑몰 고객 분석 ===")

# 실제 비즈니스 시나리오를 위한 데이터 생성
np.random.seed(2024)

# 고객 데이터 생성 (500명)
n_customers = 500

# 웹사이트 방문 시간 (분)
visit_time = np.random.exponential(15, n_customers)  # 지수분포 (현실적인 방문시간 분포)

# 방문시간에 비례하는 구매 확률로 구매액 생성
purchase_prob = 1 / (1 + np.exp(-(visit_time - 10) / 5))  # 시그모이드 함수
purchase_amount = np.where(
    np.random.random(n_customers) < purchase_prob,
    visit_time * np.random.uniform(1000, 3000, n_customers),  # 구매한 경우
    0  # 구매하지 않은 경우
)

# 고객 등급 생성
customer_grade = np.random.choice(['브론즈', '실버', '골드', '플래티넘'],
                                  n_customers, p=[0.4, 0.3, 0.2, 0.1])

# 💡 실전 데이터 생성 기법:
# - 지수분포: 방문시간, 대기시간 등에 현실적
# - 시그모이드 함수: 확률 모델링에 유용
# - np.where(): 조건에 따른 값 할당

plt.figure(figsize=(14, 6))

# 8-1. 방문시간 vs 구매액 (구매 여부로 색상 구분)
plt.subplot(1, 2, 1)

# 구매한 고객과 안 한 고객 구분
purchased = purchase_amount > 0
non_purchased = purchase_amount == 0

plt.scatter(visit_time[non_purchased], purchase_amount[non_purchased],
            alpha=0.6, color='lightgray', s=20, label='구매 안함')
plt.scatter(visit_time[purchased], purchase_amount[purchased],
            alpha=0.7, color='red', s=30, label='구매함')

plt.title('방문시간 vs 구매액\n(구매 여부별 구분)', fontsize=12, fontweight='bold')
plt.xlabel('방문시간 (분)')
plt.ylabel('구매액 (원)')
plt.legend()
plt.grid(True, alpha=0.3)

# 8-2. 고객등급별 분석
plt.subplot(1, 2, 2)

grade_colors = {'브론즈': '#CD7F32', '실버': '#C0C0C0',
                '골드': '#FFD700', '플래티넘': '#E5E4E2'}

for grade in ['브론즈', '실버', '골드', '플래티넘']:
    mask = customer_grade == grade
    plt.scatter(visit_time[mask], purchase_amount[mask],
                alpha=0.7, color=grade_colors[grade],
                s=40, label=f'{grade} 등급')

plt.title('고객등급별 방문시간 vs 구매액', fontsize=12, fontweight='bold')
plt.xlabel('방문시간 (분)')
plt.ylabel('구매액 (원)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# 9. 산점도 분석 결과 해석 가이드
# ============================================================================
print("\n=== 산점도 분석 결과 해석 가이드 ===")
print("1. 점들의 분포 패턴 관찰:")
print("   • 직선 형태: 선형 상관관계")
print("   • 곡선 형태: 비선형 관계")
print("   • 무작위 분포: 상관관계 없음")
print()
print("2. 상관관계 강도 판단:")
print("   • 점들이 직선에 가까울수록 강한 상관관계")
print("   • 점들이 넓게 퍼져있을수록 약한 상관관계")
print()
print("3. 이상치 발견:")
print("   • 전체 패턴에서 벗어난 점들 확인")
print("   • 데이터 오류 또는 특별한 케이스일 가능성")
print()
print("4. 군집(클러스터) 식별:")
print("   • 점들이 그룹을 이루는 패턴")
print("   • 고객 세분화, 제품 분류 등에 활용")

# ============================================================================
# 10. 학습 요약
# ============================================================================
print("\n=== 산점도 학습 요약 ===")
print("1. plt.scatter(): 산점도 그리기 기본 함수")
print("2. 불리언 마스킹: 조건에 맞는 데이터 선택")
print("3. 다차원 정보 표현: 색상, 크기, 모양으로 추가 정보")
print("4. 상관관계 분석: 양/음의 상관관계, 무상관 판별")
print("5. 실전 활용: 고객 분석, 성과 분석, 패턴 발견")
print("6. 데이터 전처리: 랜덤 시드, 현실적 데이터 생성")
print("7. 시각적 구분: 색상과 마커로 그룹 구분")
print("8. 비즈니스 인사이트: 데이터 패턴을 통한 의사결정 지원")