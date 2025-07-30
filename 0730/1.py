from datetime import datetime, timedelta, date
import time
import math
import random
now = datetime.today()
# 현재 시간
print(now)
# 현재 년도
print(now.year)
# 현재 달
print(now.month)
# 현재 일
print(now.day)
# 현재 시
print(now.hour)
# 현재 분
print(now.minute)
# 현재 초
print(now.second)

# 날짜 출력
print(f"{now.year}년 {now.month}월 {now.day}일")
print(f"{now.hour}시 {now.minute}분 {now.second}초")

# 특정 날짜 계산
next_week = now + timedelta(weeks=1, days=1)
print(f"1주일 후 : {next_week}")

formatted_date = now.strftime("%Y-%m-%d, %H:%M:%S")
print("formatted_date ",formatted_date)

first_day = date(year = 2025, month=8, day=1)
print("first_day", first_day)

today = date.today()
print("today", today)
print("today.weekday()", today.weekday())

passed_time = today - first_day
print(passed_time, "일 지났습니다.")

print("현재시간(초)", time.time())
print("현재시간(초)", time.localtime())

print("5초 대기중...")
time.sleep(5)
print("5초 대기 완료!")

start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print(f"소요 시간: {end - start: .2f}초")

print(math.pi)
# 제곱근
print(math.sqrt(25))
# 3!
print(math.factorial(3))
# 올림
print(math.ceil(2.6))
# 반올림
print(round(2.6))
# 버림
print(math.floor(4.7))

# 1부터 10까지의 임의의 정수 리턴
rand_int = random.randint(1, 10)
print(f"rand_int: {rand_int}")
# 1부터 10까지의 임의의 실수 리턴
rand_float = random.uniform(1,10)
print(f"rand_float: {rand_float}")
# 0 부터 1사이 임의의 실수
rand_between = random.random()
print(f"rand_between: {rand_between}")
# 200 부터 2000 사이 임의의 실수 리턴
rand_range = random.randrange(200, 2000)

choices = ["사과", "바나나", "포도", "귤", "복숭아"]
rand_choice =random.choice(choices)
print(f"rand_choice: {rand_choice}")
# 로또 번호 뽑기
lotto = random.sample(range(1,46),6)
lotto.sort()
print(lotto)