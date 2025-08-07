import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt 

plt.rcParams['font.family'] = ['DejaVu Sans', 'Malgun Gothic']  
plt.rcParams['axes.unicode_minus'] = False 

# df1=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.01.csv', encoding='cp949')
# df2=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.02.csv', encoding='cp949')
# df3=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.03.csv', encoding='cp949')
# df4=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.04.csv', encoding='cp949')
# df5=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.05.csv', encoding='cp949')
# df6=pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.06.csv', encoding='cp949')
# df_all = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index = False)

# # 날짜 형식 변환
# df_all['대여일자'] = df_all['대여일자'].str.replace('-', '')

# # 이용권 이름 변환
# df_all['대여구분코드'] = df_all['대여구분코드'].replace({
#     '일일(회원)': '일일권',
#     '정기': '정기권',
#     '일일(비회원)' : '일일권'
# })
# df_all.to_csv('서울특별시_공공자전거_이용정보(월별)_22.1-6.csv', encoding='cp949')

# df_24_1_6 = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_24.1-6.csv', encoding='cp949')
# df_24_7_12 = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_24.7-12.csv', encoding='cp949')
# df_23_1_6 = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_23.1-6.csv', encoding='cp949')
# df_23_7_12 = pd.read_csv('서울특별시_공공자전거_이용정보(월별)_23.7-12.csv', encoding='cp949')
# df_22_1_6 = pd.read_csv('서울특별시_공공자전거_이용정보(월별)_22.1-6.csv', encoding='cp949')
# df_22_7_12 = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_22.07_22.12.csv', encoding='cp949')

# df_all = pd.concat([df_24_1_6, df_24_7_12,df_23_1_6, df_23_7_12, df_22_1_6, df_22_7_12], ignore_index=False)
# df_all.to_csv('서울특별시_공공자전거_이용정보(월별)_22-24.csv', encoding='cp949')

df_all = pd.read_csv('서울특별시_공공자전거_이용정보(월별)_22-24.csv', encoding='cp949')

monthly_total = df_all.groupby('대여일자')['이용건수'].sum()
monthly_total.index = pd.to_datetime(monthly_total.index, format='%Y%m')
monthly_total = monthly_total.sort_index()

# 시계열 데이터
result = seasonal_decompose(monthly_total, model='additive', period=12)
fig = result.plot()
fig.set_size_inches(10, 6) 
plt.tight_layout()
plt.show()
# 이동 평균 계산 (3개월, 6개월)
df_monthly = pd.DataFrame({'이용건수': monthly_total})

df_monthly['MA_3'] = df_monthly['이용건수'].rolling(window=3).mean()
df_monthly['MA_6'] = df_monthly['이용건수'].rolling(window=6).mean()

plt.figure(figsize=(12, 6))
plt.plot(df_monthly.index, df_monthly['이용건수'], color='skyblue', label='이용건수', linewidth=2)
plt.fill_between(df_monthly.index, df_monthly['이용건수'], color='skyblue', alpha=0.2)
plt.plot(df_monthly['MA_3'], label='3개월 이용평균', color='orange', linewidth=3)
plt.plot(df_monthly['MA_6'], label='6개월 이용평균', color='green', linewidth=3)
plt.title('월별 공공자전거 이용 평균 시각화')
plt.xlabel('사용월')
plt.ylabel('총 이용객 수')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# 선형 회귀 분석
df_monthly['월번호'] = np.arange(len(df_monthly))
x = df_monthly['월번호']
y = df_monthly['이용건수']

# 1차 다항 회귀 (선형 회귀)
a, b  = np.polyfit(x, y, deg=1)

# 미래 6개월 예측
future_x = np.arange(len(x) + 6) 
future_y = a * future_x + b

# 날짜 인덱스 생성 (예측 포함)
future_dates = pd.date_range(
    start=df_monthly.index.min(),
    periods=len(future_x),
    freq='MS'
)

# 미래 예측 시각화
plt.figure(figsize=(12, 6))
plt.plot(df_monthly.index, y, label='이용 건수', color='skyblue')
plt.fill_between(df_monthly.index, df_monthly['이용건수'], color='skyblue', alpha=0.2)
plt.plot(future_dates, future_y, label='선형 추세선 (예측 포함)', color='red', linestyle='--', linewidth=3)
plt.title('선형 추세선 기반 공공 자전거 수요 예측')
plt.xlabel('월')
plt.ylabel('총 이용객 수')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()