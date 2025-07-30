import sys
import os
import json

print(sys.version)
print(sys.argv)

# sys.exit(0)
# print("이 문장이 나올까요??")

print("현재 디렉토리:", os.getcwd())

# json 형식
data = {
    "name" : "홍길동",
    "age" : 25,
    "city" : "서울" 
}

json_str = json.dumps(data)
print("json_str", json_str)

json_obj = json.loads(json_str)
print("python 객체", json_obj)
print(json_obj["name"])