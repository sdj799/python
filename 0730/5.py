# 예외(Exception)
# 프로그램 실행 중에 발생하는 오류나 예상치 못한 상황
try:
    # 예외가 발생할 수 있는 코드
    pass
except:
    # 예외 처리 코드
    pass

try:
    result = 10/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
try:
    result = [1,2,3]
    print(result[5])
except IndexError:
    print("리스트 범위를 벗어났습니다.")

try:
    person = {"name": "김철수", "age": 25,}
    print(person["address"])
except KeyError:
    print("존재하지 않는 키 입니다.")

try:
    result = "문자열" + 100
except TypeError:
    print("타입이 맞지 않습니다.")

try:
    result = 10/1
    if result == 10:
        raise Exception('에러 발생 할 수 있습니다')
except IndexError:
    print("리스트 범위를 벗어났습니다.")
except KeyError:
    print("존재하지 않는 키 입니다.")
except Exception as e :
    print(e)
else:
    # 예외가 발생하지 않았을때 실행
    print("else 입니다.")
finally:
    print("finally 입니다")