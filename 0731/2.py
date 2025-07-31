import numpy as np

sales = np.array([[120, 135, 148, 162],  # 서울점
                  [98, 110, 125, 140],   # 부산점  
                  [75, 82, 95, 110]])    # 대구점

branches = ['서울점', '부산점', '대구점']
# 행마다 최댓값
print(np.max(sales, axis=1))
# 열 마다 최댓값
print(np.max(sales, axis=0))
print("각 지점별 최고 매출 달과 금액")
for i, branche in enumerate(branches):
    max_idx = np.argmax(sales[i])
    max_sales = sales[i, max_idx]
    print(f"{branche}: {max_idx + 1}분기 {max_sales}")

print("100 이상인 매출 데이터만 추출:", sales[sales >= 100])
print("서울점의 2,4분기 매출: ", sales[0,[1,3]])
sales[:,2] = 105
print("모든 지점의 3분기 매출을 105로 수정", sales)