import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams['font.family'] = ['DejaVu Sans', 'Malgun Gothic']  
plt.rcParams['axes.unicode_minus'] = False 

# 월별 이용정보

df = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_24.1-6.csv', encoding='cp949')
df2 = pd.read_csv('서울특별시 공공자전거 이용정보(월별)_24.7-12.csv', encoding='cp949')
df_all = pd.concat([df, df2], ignore_index = False)
df_code_month = df_all.groupby(['대여구분코드','대여일자'])['이용건수'].sum().unstack(0)
df_all['대여구분코드'] = df_all['대여구분코드'].replace({'일일권(비회원)': '일일권'})
df_code_month = df_all.groupby(['대여구분코드','대여일자'])['이용건수'].sum().unstack(0)

print(df_code_month)

month_labels = [f'{int(str(m)[4:])}월' for m in df_code_month.index]

# 막대 위치 설정
x = range(len(df_code_month.index))
bar_width = 0.4

# 정기권 일일권 월별 그래프
plt.figure(figsize=(12, 6))

plt.bar([i - bar_width/2 for i in x], df_code_month['일일권'], width=bar_width, label='일일권 (전체)', color='skyblue')
plt.bar([i + bar_width/2 for i in x], df_code_month['정기권'], width=bar_width, label='정기권', color='orange')
plt.xticks(x, month_labels, rotation=0)
plt.title('2024년도 월별 정기권, 일일권 이용건수')
plt.xlabel('월')
plt.ylabel('이용건수(백만)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# 대여소별 이용정보

df = pd.read_csv('서울특별시 공공자전거 대여소별 이용정보(월별)_24.1-6.csv', encoding='cp949')
df1 = pd.read_csv('서울특별시 공공자전거 대여소별 이용정보(월별)_24.7-12.csv', encoding='cp949')
df_all = pd.concat([df, df1], ignore_index = False)
df_location = df_all.groupby('자치구')[['대여건수', '반납건수']].sum()
df_location['회수율'] = df_location['반납건수'] / df_location['대여건수'] * 100
df_location_sorted = df_location.sort_values(by='대여건수', ascending=False)

print(df_location_sorted)

# 대여소별 그래프
fig, ax1 = plt.subplots(figsize=(14, 7))
x = np.arange(len(df_location_sorted.index))
width = 0.3

bar1 = ax1.bar(x - width/2, df_location_sorted['대여건수'],width=width, color='skyblue')
bar2 = ax1.bar(x + width/2, df_location_sorted['반납건수'],width=width, color='salmon')

ax2 = ax1.twinx()
line = ax2.plot(x, df_location_sorted['회수율'], color='green', marker='o', linewidth=1, label='회수율')

ax2.axhline(0, color='gray', linestyle='--', linewidth=1)
ax2.set_ylim(92, 108)

ax1.set_xlabel('자치구')
ax1.set_ylabel('건수(백만)')
ax1.set_title('2024년도 대여소별 이용정보')
ax1.set_xticks(x)
ax1.set_xticklabels(df_location_sorted.index, rotation=60)
ax1.legend()

lines_labels = [*zip([bar1, bar2], ['대여건수', '반납건수']), (line[0], '회수율')]
handles, labels = zip(*lines_labels)
ax1.legend(handles, labels, loc='upper right')
plt.tight_layout()
plt.show()

