
# enumerate
# 반복 가능한 객체를 받아서 인덱스와 값을 함께 반환하는 내장 함수

nums = [1,2,3,4,5,6]
for i, num in enumerate(nums, 1):
    print(f"인덱스: {i}, 값: {num}")

fruits = ["사과", "바나나", "수박", "포도", "복숭아"]
for i, fruit in enumerate(fruits):
    print(f"인덱스: {i}, 값: {fruit}")