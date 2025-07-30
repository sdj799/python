# ============================================================
# Python 파일 입출력 완전 가이드
# ============================================================

import os
import json

print("=" * 60)
print("📂 Python 파일 입출력 학습")
print("=" * 60)

# ============================================================
# 1. 파일이란? - 기본 개념
# ============================================================

print("\n📖 1. 파일이란?")
print("-" * 40)

"""
파일(File)이란?
- 컴퓨터에 정보를 저장하는 기본 단위
- 데이터를 디스크에 영구적으로 보관할 수 있게 해주는 컨테이너
- 프로그램이 종료되어도 데이터가 사라지지 않음

파일의 종류:
1. 텍스트 파일: .txt, .py, .html, .css, .json, .csv 등
2. 바이너리 파일: .jpg, .mp3, .exe, .pdf 등
"""

# 메모리 vs 파일 저장 차이점 보여주기
students = ["김철수", "이영희", "박민수"]
print(f"메모리의 학생 목록: {students}")
print("⚠️ 프로그램이 종료되면 메모리의 모든 데이터는 사라집니다!")
print("💾 파일에 저장하면 영구적으로 보관할 수 있습니다.")

# ============================================================
# 2. 기본 파일 입출력 - open(), write(), close()
# ============================================================

print("\n✍️ 2. 기본 파일 입출력")
print("-" * 40)

# 방법 1: 기본적인 파일 열기/쓰기/닫기
print("📝 방법 1: 기본적인 파일 처리")

# 파일 열기 (쓰기 모드)
file = open("example_basic.txt", "w", encoding="utf-8")

# 파일에 내용 쓰기
file.write("안녕하세요! 파이썬 파일 입출력입니다.")

# 파일 닫기 (중요!)
file.close()

print("✅ 'example_basic.txt' 파일이 생성되었습니다.")

# 방법 2: with문을 사용한 안전한 파일 처리 (권장)
print("\n📝 방법 2: with문을 사용한 안전한 파일 처리 (권장)")

with open("example_with.txt", "w", encoding="utf-8") as file:
    file.write("with문을 사용한 안전한 파일 처리입니다.")

print("✅ 'example_with.txt' 파일이 생성되었습니다.")
print("💡 with문의 장점: 자동으로 파일이 닫혀서 메모리 누수 방지")

# 여러 줄 쓰기
print("\n📝 여러 줄 쓰기 예제")

with open("example_multiline.txt", "w", encoding="utf-8") as file:
    lines = [
        "첫 번째 줄입니다.\n",
        "두 번째 줄입니다.\n",
        "세 번째 줄입니다.\n"
    ]
    file.writelines(lines)  # 여러 줄을 한 번에 쓰기

print("✅ 여러 줄이 포함된 파일이 생성되었습니다.")

# ============================================================
# 3. 파일 경로 - 절대 경로 vs 상대 경로
# ============================================================

print("\n🗺️ 3. 파일 경로 - 절대 경로 vs 상대 경로")
print("-" * 40)

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print(f"📁 현재 작업 디렉토리: {current_dir}")

print(f"\n📋 경로의 종류:")
print(f"1. 절대 경로 (Absolute Path):")
print(f"   - 루트 디렉토리부터 시작하는 전체 경로")
print(f"   - Windows 예: C:\\Users\\사용자\\Desktop\\파일.txt")
print(f"   - Linux/Mac 예: /home/사용자/Desktop/파일.txt")

print(f"\n2. 상대 경로 (Relative Path):")
print(f"   - 현재 위치를 기준으로 하는 경로")
print(f"   - './파일.txt' : 현재 폴더의 파일")
print(f"   - '../파일.txt' : 상위 폴더의 파일")
print(f"   - './하위폴더/파일.txt' : 하위 폴더의 파일")

# 하위 디렉토리에 파일 생성 예제
sub_directory = "test_folder"
if not os.path.exists(sub_directory):
    os.makedirs(sub_directory)
    print(f"📁 '{sub_directory}' 디렉토리를 생성했습니다.")

# 하위 폴더에 파일 생성
sub_file_path = os.path.join(sub_directory, "sub_example.txt")
with open(sub_file_path, "w", encoding="utf-8") as file:
    file.write("하위 디렉토리에 있는 파일입니다.")

print(f"✅ '{sub_file_path}' 파일이 생성되었습니다.")

# ============================================================
# 4. 파일 읽기 - read(), readline(), readlines()
# ============================================================

print("\n📖 4. 파일 읽기 방법들")
print("-" * 40)

# 읽기용 테스트 파일 생성
test_content = """첫 번째 줄입니다.
두 번째 줄입니다.
세 번째 줄입니다.
네 번째 줄입니다."""

with open("read_test.txt", "w", encoding="utf-8") as file:
    file.write(test_content)

print("📝 테스트 파일 'read_test.txt'를 생성했습니다.")

# 방법 1: read() - 전체 파일 내용을 한 번에 읽기
print(f"\n📖 방법 1: file.read() - 전체 내용 읽기")
with open("read_test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"파일 전체 내용:")
    print(f"'{content}'")

# 방법 2: readline() - 한 줄씩 읽기
print(f"\n📖 방법 2: file.readline() - 한 줄씩 읽기")
with open("read_test.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"첫 번째 줄: '{line1.strip()}'")  # strip()으로 줄바꿈 제거
    print(f"두 번째 줄: '{line2.strip()}'")

# 방법 3: readlines() - 모든 줄을 리스트로 읽기
print(f"\n📖 방법 3: file.readlines() - 모든 줄을 리스트로 읽기")
with open("read_test.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"모든 줄 (리스트): {lines}")
    print(f"줄 개수: {len(lines)}개")


# 방법 4: for문으로 한 줄씩 처리 (메모리 효율적)
print(f"\n📖 방법 4: for문으로 한 줄씩 처리 (권장)")
with open("read_test.txt", "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
        print(f"{line_num}번째 줄: '{line.strip()}'")


# ============================================================
# 5. 파일 모드 (File Modes)
# ============================================================

print("\n🔧 5. 파일 모드 (File Modes)")
print("-" * 40)

file_modes = {
    "r": "읽기 전용 (파일이 존재해야 함)",
    "w": "쓰기 전용 (기존 내용 덮어쓰기)",
    "a": "추가 모드 (기존 내용 뒤에 추가)",
    "x": "배타적 생성 (파일이 없을 때만 생성)",
    "r+": "읽기+쓰기 (파일이 존재해야 함)",
    "w+": "읽기+쓰기 (기존 내용 덮어쓰기)",
    "a+": "읽기+추가 (기존 내용 뒤에 추가)"
}

print("📋 파일 모드 설명:")
for mode, description in file_modes.items():
    print(f"  '{mode}': {description}")

# 추가 모드 예제
print(f"\n📝 추가 모드 ('a') 예제:")
with open("append_test.txt", "w", encoding="utf-8") as file:
    file.write("첫 번째 내용\n")

with open("append_test.txt", "a", encoding="utf-8") as file:
    file.write("두 번째 내용 (추가됨)\n")
    file.write("세 번째 내용 (추가됨)\n")

# 결과 확인
with open("append_test.txt", "r", encoding="utf-8") as file:
    print("추가 모드 결과:")
    print(file.read())

# ============================================================
# 6. 실제 활용 예제들
# ============================================================

print("\n🎯 6. 실제 활용 예제들")
print("-" * 40)

# 예제 1: 학생 성적 관리 시스템


def save_student_scores():
    """학생 성적을 파일에 저장"""
    students = [
        {"name": "김철수", "korean": 85, "english": 90, "math": 78},
        {"name": "이영희", "korean": 92, "english": 88, "math": 95},
        {"name": "박민수", "korean": 78, "english": 85, "math": 82}
    ]

    with open("student_scores.txt", "w", encoding="utf-8") as file:
        file.write("학생 성적표\n")
        file.write("=" * 40 + "\n")
        file.write(f"{'이름':8} {'국어':>6} {'영어':>6} {'수학':>6} {'평균':>6}\n")
        file.write("-" * 40 + "\n")

        for student in students:
            avg = (student['korean'] +
                   student['english'] + student['math']) / 3
            file.write(
                f"{student['name']:8} {student['korean']:6} {student['english']:6} {student['math']:6} {avg:6.1f}\n")

    print("✅ 학생 성적이 'student_scores.txt'에 저장되었습니다.")


save_student_scores()

# 예제 2: 로그 파일 기록


def write_log(message, level="INFO"):
    """로그 메시지를 파일에 기록"""
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"

    with open("application.log", "a", encoding="utf-8") as file:
        file.write(log_entry)


print(f"\n📝 로그 시스템 예제:")
write_log("애플리케이션이 시작되었습니다.", "INFO")
write_log("사용자가 로그인했습니다.", "INFO")
write_log("데이터베이스 연결 오류가 발생했습니다.", "ERROR")

# 로그 파일 내용 확인
try:
    with open("application.log", "r", encoding="utf-8") as file:
        print("로그 파일 내용:")
        print(file.read())
except FileNotFoundError:
    print("로그 파일이 없습니다.")

# 예제 3: CSV 파일 읽기/쓰기


def create_csv_example():
    """CSV 형태의 데이터 파일 생성"""
    csv_data = """이름,나이,도시,직업
김철수,25,서울,개발자
이영희,30,부산,디자이너
박민수,28,대구,기획자
최영준,35,인천,마케터"""

    with open("employees.csv", "w", encoding="utf-8") as file:
        file.write(csv_data)

    print("✅ CSV 파일 'employees.csv'가 생성되었습니다.")


def read_csv_example():
    """CSV 파일 읽기 예제"""
    try:
        with open("employees.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()

            # 헤더 분리
            header = lines[0].strip().split(',')
            print(f"CSV 헤더: {header}")

            # 데이터 처리
            print("\n직원 정보:")
            for line in lines[1:]:
                data = line.strip().split(',')
                employee = dict(zip(header, data))
                print(
                    f"  {employee['이름']} ({employee['나이']}세, {employee['도시']}, {employee['직업']})")

    except FileNotFoundError:
        print("CSV 파일을 찾을 수 없습니다.")


create_csv_example()
read_csv_example()

# 예제 4: 설정 파일 관리


def save_config():
    """애플리케이션 설정 저장"""
    config = {
        "theme": "dark",
        "language": "ko",
        "auto_save": True,
        "font_size": 14,
        "recent_files": [
            "document1.txt",
            "document2.txt",
            "document3.txt"
        ]
    }

    with open("app_config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=2)

    print("✅ 설정이 'app_config.json'에 저장되었습니다.")


def load_config():
    """애플리케이션 설정 읽기"""
    try:
        with open("app_config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
            print("📖 설정 파일 내용:")
            for key, value in config.items():
                print(f"  {key}: {value}")
            return config
    except FileNotFoundError:
        print("설정 파일을 찾을 수 없습니다.")
        return {}


save_config()
load_config()

# ============================================================
# 7. 파일 처리 시 주의사항과 팁
# ============================================================

print(f"\n⚠️ 7. 파일 처리 시 주의사항과 팁")
print("-" * 40)

# 예외 처리 예제


def safe_file_operation():
    """안전한 파일 처리 예제"""
    try:
        with open("nonexistent_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다.")
    except PermissionError:
        print("❌ 파일에 접근할 권한이 없습니다.")
    except UnicodeDecodeError:
        print("❌ 파일 인코딩 문제가 발생했습니다.")
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")


print("🔒 안전한 파일 처리 예제:")
safe_file_operation()

# 파일 존재 여부 확인


def check_file_exists(filename):
    """파일 존재 여부 확인"""
    if os.path.exists(filename):
        print(f"✅ '{filename}' 파일이 존재합니다.")

        # 파일 정보 출력
        file_stat = os.stat(filename)
        print(f"   파일 크기: {file_stat.st_size} bytes")

        import datetime
        mod_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)
        print(f"   수정 시간: {mod_time}")
    else:
        print(f"❌ '{filename}' 파일이 존재하지 않습니다.")


print(f"\n📋 파일 존재 여부 확인:")
check_file_exists("read_test.txt")
check_file_exists("nonexistent_file.txt")

# ============================================================
# 8. 정리 및 베스트 프랙티스
# ============================================================

print(f"\n💡 8. 정리 및 베스트 프랙티스")
print("-" * 40)

best_practices = [
    "항상 with문을 사용해서 파일을 자동으로 닫기",
    "인코딩을 명시적으로 지정 (encoding='utf-8')",
    "파일 작업 시 try-except로 예외 처리하기",
    "파일 경로는 os.path.join()으로 안전하게 조합",
    "큰 파일은 한 번에 읽지 말고 한 줄씩 처리",
    "파일 모드를 정확히 이해하고 사용하기",
    "중요한 데이터는 백업 파일도 함께 생성",
    "임시 파일은 작업 완료 후 정리하기"
]

for i, practice in enumerate(best_practices, 1):
    print(f"💡 {i}. {practice}")

# 생성된 테스트 파일들 정리
print(f"\n🗑️ 테스트 파일 정리:")
test_files = [
    "example_basic.txt", "example_with.txt", "example_multiline.txt",
    "read_test.txt", "append_test.txt", "student_scores.txt",
    "application.log", "employees.csv", "app_config.json"
]

for filename in test_files:
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"🗑️ '{filename}' 삭제됨")
        except Exception as e:
            print(f"❌ '{filename}' 삭제 실패: {e}")

# 테스트 폴더도 정리
if os.path.exists("test_folder"):
    try:
        if os.path.exists(os.path.join("test_folder", "sub_example.txt")):
            os.remove(os.path.join("test_folder", "sub_example.txt"))
        os.rmdir("test_folder")
        print(f"🗑️ 'test_folder' 디렉토리 삭제됨")
    except Exception as e:
        print(f"❌ 'test_folder' 삭제 실패: {e}")

print("\n" + "=" * 60)
print("🎉 Python 파일 입출력 학습 완료!")
print("=" * 60)