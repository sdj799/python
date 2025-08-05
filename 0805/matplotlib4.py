# Matplotlib 히스토그램(Histogram) 강의 자료
# 데이터의 분포를 한눈에 파악하는 가장 기본적이고 중요한 도구

import matplotlib.pyplot as plt  # 그래프 그리기 위한 pyplot 모듈
import numpy as np               # 수치 계산과 통계 분석을 위한 NumPy

# ============================================================================
# 1. 한글 폰트 설정 (한글 깨짐 방지)
# ============================================================================
plt.rcParams['font.family'] = ['DejaVu Sans', 'Malgun Gothic']  # 폰트 우선순위 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# ============================================================================
# 2. 히스토그램이란 무엇인가?
# ============================================================================
print("=== 히스토그램(Histogram) 개념 ===")
print("• 연속형 데이터의 분포를 막대로 표현하는 그래프")
print("• 데이터가 어떤 값 구간에 얼마나 많이 분포되어 있는지 보여줌")
print("• 데이터의 중심, 퍼짐, 치우침, 이상치를 파악할 수 있음")
print()

# 💡 히스토그램 vs 막대그래프 차이점:
# - 히스토그램: 연속형 데이터의 구간별 빈도 (키, 점수, 나이 등)
# - 막대그래프: 범주형 데이터의 카테고리별 값 (지역별 매출, 제품별 판매량 등)

# 💡 히스토그램 활용 분야:
# - 품질관리: 제품 사이즈, 무게 분포 확인
# - 교육: 학생 성적 분포 분석
# - 마케팅: 고객 연령, 구매액 분포 분석
# - 의학: 환자 혈압, 체중 분포 연구

# ============================================================================
# 3. 첫 번째 예제: 학급 학생들의 키 분포
# ============================================================================
print("=== 첫 번째 예제: 반 학생들의 키 분포 분석 ===")

# 실제 학급 상황을 시뮬레이션한 키 데이터 (20명의 학생)
heights = [160, 162, 158, 165, 170, 168, 163, 167, 169, 164,
           161, 166, 172, 159, 163, 165, 168, 170, 164, 167]

print('반 학생들의 키 (정렬 전):')
print(heights)

# 데이터 정렬하여 분포 파악
heights_sorted = sorted(heights)  # 원본 데이터는 보존하고 새로운 정렬된 리스트 생성
print('\\n반 학생들의 키 (정렬 후):')
print(heights_sorted)

# 💡 기본 통계량 계산 및 출력
print(f'\\n=== 기본 통계량 ===')
print(f'최솟값: {min(heights)}cm')
print(f'최댓값: {max(heights)}cm')
print(f'평균: {np.mean(heights):.1f}cm')
print(f'중앙값: {np.median(heights):.1f}cm')
print(f'표준편차: {np.std(heights):.1f}cm')
print(f'범위: {max(heights) - min(heights)}cm')
print()

# 히스토그램 그리기
plt.figure(figsize=(10, 6))

# 기본 히스토그램 생성
n, bins, patches = plt.hist(heights,           # 데이터
                            bins=5,             # 구간(bin) 개수
                            color='lightblue',  # 막대 색상
                            edgecolor='black',  # 막대 테두리 색상
                            alpha=0.7)          # 투명도

# 💡 plt.hist() 반환값:
# - n: 각 구간의 빈도수 (막대 높이)
# - bins: 구간의 경계값들
# - patches: 막대 객체들 (색상 변경 등에 사용)

print(f"각 구간의 빈도수: {n}")
print(f"구간 경계값: {bins}")
print()

plt.title('반 학생들 키 분포', fontsize=16, fontweight='bold')
plt.xlabel('키 (cm)', fontsize=12)
plt.ylabel('학생 수 (명)', fontsize=12)
plt.grid(True, alpha=0.5)

# 평균선 추가 (분포의 중심 표시)
mean_height = np.mean(heights)
plt.axvline(mean_height, color='red', linestyle='--',
            linewidth=2, label=f'평균: {mean_height:.1f}cm')
plt.legend()

# 💡 plt.axvline(): 수직선 그리기
# - 히스토그램에서 평균, 중앙값 등 기준선 표시에 유용
# - axhline(): 수평선 그리기

plt.show()

# ============================================================================
# 4. 두 번째 예제: 빈(bin) 개수의 중요성
# ============================================================================
print("=== 빈(bin) 개수가 히스토그램에 미치는 영향 ===")

# 랜덤 시드 설정으로 재현 가능한 데이터 생성
np.random.seed(42)

# 학생 시험 점수 데이터 (30명)
student_scores = [65, 72, 78, 81, 69, 88, 92, 76, 83, 70,
                  74, 79, 85, 68, 91, 77, 82, 73, 86, 75,
                  80, 84, 71, 89, 67, 93, 78, 81, 74, 87]

print(f"학생 시험 점수 ({len(student_scores)}명):")
print(f"최고점: {max(student_scores)}점")
print(f"최저점: {min(student_scores)}점")
print(f"평균: {np.mean(student_scores):.1f}점")
print(f"표준편차: {np.std(student_scores):.1f}점")
print()

# 서로 다른 빈 개수로 비교 분석
plt.figure(figsize=(15, 5))

bin_counts = [3, 6, 10]                           # 빈 개수 옵션
titles = ['빈이 너무 적음 (3개)', '적당한 빈 (6개)', '빈이 너무 많음 (10개)']
colors = ['lightcoral', 'lightblue', 'lightgreen']  # 각각 다른 색상

for i, (bin_count, title, color) in enumerate(zip(bin_counts, titles, colors)):
    plt.subplot(1, 3, i+1)  # 1행 3열의 서브플롯

    # 히스토그램 그리기
    n, bins, patches = plt.hist(student_scores,
                                bins=bin_count,
                                color=color,
                                edgecolor='black',
                                alpha=0.7)

    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel('점수', fontsize=10)
    plt.ylabel('학생 수', fontsize=10)
    plt.grid(True, alpha=0.3)

    # 각 구간의 빈도수 출력
    print(f"{title}: 빈도수 {n}")

print()

# 💡 적절한 빈 개수 선택 가이드:
print("=== 빈 개수 선택 가이드 ===")
print("• 너무 적으면: 세부 패턴을 놓칠 수 있음")
print("• 너무 많으면: 노이즈가 많아져 전체 패턴 파악 어려움")
print("• 경험적 법칙: √n (데이터 개수의 제곱근) 또는 5~20개 사이")
print(
    f"• 현재 데이터({len(student_scores)}개): 권장 빈 개수 약 {int(np.sqrt(len(student_scores)))}개")
print()

plt.tight_layout()
plt.show()

# ============================================================================
# 5. 다양한 분포 패턴 분석
# ============================================================================
print("=== 다양한 분포 패턴과 해석 ===")

# 서로 다른 특성을 가진 데이터셋 생성
np.random.seed(123)

# 1) 정규분포 (종 모양)
normal_data = np.random.normal(100, 15, 1000)    # 평균 100, 표준편차 15

# 2) 균등분포 (평평한 분포)
uniform_data = np.random.uniform(50, 150, 1000)  # 50~150 사이 균등분포

# 3) 치우친 분포 (비대칭 분포)
skewed_data = np.random.exponential(30, 1000)    # 지수분포 (오른쪽 치우침)

plt.figure(figsize=(15, 10))

# 💡 다양한 분포의 특징과 의미:
# - 정규분포: 자연현상, 측정값에서 자주 나타남 (키, 몸무게, IQ 등)
# - 균등분포: 모든 값이 동일한 확률로 나타남 (주사위, 복권 등)
# - 치우친 분포: 소득, 인구밀도, 반응시간 등에서 자주 나타남

# 5-1. 정규분포 (Normal Distribution)
plt.subplot(2, 3, 1)
plt.hist(normal_data, bins=30, color='lightblue', alpha=0.7, edgecolor='black')
plt.title('정규분포 (종 모양)\\n대부분 데이터가 평균 주변에 집중', fontsize=11, fontweight='bold')
plt.xlabel('값')
plt.ylabel('빈도')
plt.axvline(np.mean(normal_data), color='red', linestyle='--',
            label=f'평균: {np.mean(normal_data):.1f}')
plt.legend()
plt.grid(True, alpha=0.3)

# 5-2. 균등분포 (Uniform Distribution)
plt.subplot(2, 3, 2)
plt.hist(uniform_data, bins=30, color='lightgreen',
         alpha=0.7, edgecolor='black')
plt.title('균등분포 (평평한 분포)\\n모든 구간에 고르게 분포', fontsize=11, fontweight='bold')
plt.xlabel('값')
plt.ylabel('빈도')
plt.axvline(np.mean(uniform_data), color='red', linestyle='--',
            label=f'평균: {np.mean(uniform_data):.1f}')
plt.legend()
plt.grid(True, alpha=0.3)

# 5-3. 치우친 분포 (Skewed Distribution)
plt.subplot(2, 3, 3)
plt.hist(skewed_data, bins=30, color='lightcoral',
         alpha=0.7, edgecolor='black')
plt.title('치우친 분포 (비대칭)\\n오른쪽 꼬리가 긴 분포', fontsize=11, fontweight='bold')
plt.xlabel('값')
plt.ylabel('빈도')
plt.axvline(np.mean(skewed_data), color='red', linestyle='--',
            label=f'평균: {np.mean(skewed_data):.1f}')
plt.axvline(np.median(skewed_data), color='blue', linestyle=':',
            label=f'중앙값: {np.median(skewed_data):.1f}')
plt.legend()
plt.grid(True, alpha=0.3)

# ============================================================================
# 6. 히스토그램 고급 활용 - 그룹 비교
# ============================================================================

# 6-1. 남녀 키 분포 비교 (투명도 활용)
plt.subplot(2, 3, 4)

# 성별에 따른 키 데이터 생성 (현실적인 분포)
male_heights = np.random.normal(175, 7, 500)    # 남성: 평균 175cm, 표준편차 7
female_heights = np.random.normal(162, 6, 500)  # 여성: 평균 162cm, 표준편차 6

# 겹쳐서 그리기 (투명도 활용)
plt.hist(male_heights, bins=20, alpha=0.7,
         color='blue', label='남성', edgecolor='black')
plt.hist(female_heights, bins=20, alpha=0.7,
         color='red', label='여성', edgecolor='black')
plt.title('성별 키 분포 비교\\n(겹쳐서 그리기)', fontsize=11, fontweight='bold')
plt.xlabel('키 (cm)')
plt.ylabel('빈도')
plt.legend()
plt.grid(True, alpha=0.3)

# 6-2. 나란히 그리기 (히스토그램 타입 변경)
plt.subplot(2, 3, 5)
plt.hist([male_heights, female_heights],
         bins=20,
         color=['blue', 'red'],
         label=['남성', '여성'],
         alpha=0.7,
         edgecolor='black')
plt.title('성별 키 분포 비교\\n(나란히 그리기)', fontsize=11, fontweight='bold')
plt.xlabel('키 (cm)')
plt.ylabel('빈도')
plt.legend()
plt.grid(True, alpha=0.3)

# 6-3. 상자그림과 히스토그램 결합
plt.subplot(2, 3, 6)

# 히스토그램과 통계 정보 결합
scores_A = np.random.normal(75, 10, 200)  # A반 성적
scores_B = np.random.normal(80, 8, 200)   # B반 성적

plt.hist(scores_A, bins=15, alpha=0.6,
         color='lightblue', label='A반', density=True)
plt.hist(scores_B, bins=15, alpha=0.6,
         color='lightcoral', label='B반', density=True)

# 💡 density=True: 빈도 대신 확률밀도로 표시 (면적이 1이 되도록 정규화)
# 이렇게 하면 서로 다른 크기의 데이터셋도 비교 가능

plt.title('반별 성적 분포 비교\\n(확률밀도)', fontsize=11, fontweight='bold')
plt.xlabel('점수')
plt.ylabel('확률밀도')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# 7. 실전 비즈니스 활용 예제
# ============================================================================
print("\\n=== 실전 예제: 온라인 쇼핑몰 고객 구매 패턴 분석 ===")

# 실제 비즈니스 데이터를 모방한 시나리오
np.random.seed(2024)

# 고객 구매 데이터 생성 (1000명의 고객)
n_customers = 1000

# 구매액 분포 (현실적인 치우친 분포)
# 대부분의 고객은 적게 구매하고, 소수의 고객이 많이 구매
purchase_amounts = np.random.lognormal(mean=3, sigma=0.8, size=n_customers)
purchase_amounts = purchase_amounts * 10000  # 원 단위로 변환

# 고객 연령 분포 (정규분포에 가까움)
customer_ages = np.random.normal(35, 12, n_customers)
customer_ages = np.clip(customer_ages, 18, 70)  # 18~70세로 제한

# 💡 np.clip(): 값의 범위를 제한하는 함수
# 18세 미만은 18로, 70세 초과는 70으로 조정

plt.figure(figsize=(16, 6))

# 7-1. 구매액 분포 분석
plt.subplot(1, 3, 1)
plt.hist(purchase_amounts, bins=50, color='gold', alpha=0.7, edgecolor='black')
plt.title('고객 구매액 분포\\n(전형적인 비즈니스 패턴)', fontsize=12, fontweight='bold')
plt.xlabel('구매액 (원)')
plt.ylabel('고객 수')

# 주요 통계량 표시
mean_purchase = np.mean(purchase_amounts)
median_purchase = np.median(purchase_amounts)
plt.axvline(mean_purchase, color='red', linestyle='--',
            label=f'평균: {mean_purchase:,.0f}원')
plt.axvline(median_purchase, color='blue', linestyle=':',
            label=f'중앙값: {median_purchase:,.0f}원')
plt.legend()
plt.grid(True, alpha=0.3)

print(f"구매액 분석 결과:")
print(f"평균 구매액: {mean_purchase:,.0f}원")
print(f"중앙값 구매액: {median_purchase:,.0f}원")
print(f"최고 구매액: {max(purchase_amounts):,.0f}원")
print(f"표준편차: {np.std(purchase_amounts):,.0f}원")
print()

# 💡 치우친 분포에서는 평균 > 중앙값
# 소수의 고액 구매 고객이 평균을 끌어올림

# 7-2. 연령대별 구매 패턴
plt.subplot(1, 3, 2)
plt.hist(customer_ages, bins=25, color='lightgreen',
         alpha=0.7, edgecolor='black')
plt.title('고객 연령 분포', fontsize=12, fontweight='bold')
plt.xlabel('나이')
plt.ylabel('고객 수')
plt.axvline(np.mean(customer_ages), color='red', linestyle='--',
            label=f'평균: {np.mean(customer_ages):.1f}세')
plt.legend()
plt.grid(True, alpha=0.3)

# 7-3. 고액 구매 고객 분석 (상위 10%)
plt.subplot(1, 3, 3)
high_spenders_threshold = np.percentile(purchase_amounts, 90)  # 상위 10% 기준점
high_spenders = purchase_amounts[purchase_amounts >= high_spenders_threshold]

plt.hist(high_spenders, bins=20, color='purple', alpha=0.7, edgecolor='black')
plt.title(f'고액 구매 고객 분포\\n(상위 10%, {high_spenders_threshold:,.0f}원 이상)',
          fontsize=12, fontweight='bold')
plt.xlabel('구매액 (원)')
plt.ylabel('고객 수')
plt.grid(True, alpha=0.3)

print(f"고액 구매 고객 분석:")
print(f"상위 10% 기준: {high_spenders_threshold:,.0f}원")
print(f"고액 구매 고객 수: {len(high_spenders)}명")
print(f"고액 구매 고객 평균 구매액: {np.mean(high_spenders):,.0f}원")
print()

plt.tight_layout()
plt.show()

# ============================================================================
# 8. 히스토그램 해석 및 비즈니스 인사이트
# ============================================================================
print("=== 히스토그램 분석 결과 해석 및 비즈니스 인사이트 ===")
print()
print("1. 분포의 형태:")
print("   • 정규분포: 품질관리가 잘 되는 제품, 자연스러운 현상")
print("   • 치우친 분포: 소득, 구매액 등 경제 데이터에서 흔함")
print("   • 이봉분포: 서로 다른 두 그룹이 섞여있을 가능성")
print()
print("2. 중심 경향성:")
print("   • 평균 vs 중앙값의 차이로 분포의 치우침 정도 파악")
print("   • 치우진 분포에서는 중앙값이 더 대표적인 값")
print()
print("3. 비즈니스 활용:")
print("   • 고객 세분화: 구매 패턴에 따른 타겟 마케팅")
print("   • 재고 관리: 수요 분포 파악으로 최적 재고량 결정")
print("   • 가격 전략: 고객 지불의향 분포 분석")
print("   • 품질 개선: 불량률 분포 모니터링")

# ============================================================================
# 9. 학습 요약
# ============================================================================
print("\\n=== 히스토그램 학습 요약 ===")
print("1. plt.hist(): 히스토그램 그리기 기본 함수")
print("2. bins 매개변수: 구간 개수 조정으로 적절한 세밀도 설정")
print("3. 분포 패턴 해석: 정규분포, 균등분포, 치우친 분포 특징")
print("4. 통계량 표시: 평균, 중앙값 선으로 기준점 제공")
print("5. 그룹 비교: 투명도와 색상으로 여러 분포 동시 분석")
print("6. density 매개변수: 확률밀도로 서로 다른 크기 데이터 비교")
print("7. 실전 활용: 고객 분석, 품질관리, 재고관리 등")
print("8. 비즈니스 인사이트: 데이터 분포를 통한 의사결정 지원")
print("9. 이상치 탐지: 분포에서 벗어난 값들의 패턴 분석")
print("10. 데이터 전처리: np.clip(), np.percentile() 등 활용")