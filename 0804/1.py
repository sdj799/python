# CSV
# Cooma Seperate Values 가장 일반적인 데이터 파일 형식
# 쉼표(,)로 값들 분류

import pandas as pd

try:
    df = pd.read_csv('pandas_csv.csv', 
                     encoding='utf-8', 
                     sep=",", #구분자(기본값: 쉼표)
                     header=0, # 헤더 행 번호
                     index_col=0, # 인덱스로 사용할 열 번호
                     names=['A','B','C','D'], # 직접 컬럼명 지정
                     skiprows=1, # n개 건너뛰기
                     nrows=2, # n행만 읽기
                     na_values=['N/A'], # 결측값으로 처리할 값들
                     )
    print(df)

    df.to_csv('output.csv', encoding='utf-8', index=False)
except:
    print("파일을 찾을 수 없습니다.")

try:
    df = pd.read_json('pandas_json.json')
    print(df)
    df.to_json('output.json', orient='records', force_ascii=False)
except:
    print("파일을 찾을 수 없습니다.")

book_data = pd.DataFrame({
    '도서명': ['파이썬 기초', '데이터 분석', '머신러닝', '웹 개발', '소설 읽기'],
    '저자': ['김파이썬', '박데이터', '이머신', '최웹개발', '한소설'],
    '가격': [25000, 30000, 35000, 28000, 15000],
    '재고': [20, 15, 10, 25, 30],
    '분야': ['IT', 'IT', 'IT', 'IT', '문학']
})
try:
    book_data.to_csv('library_books.csv', encoding='utf-8', index=False)
except(Exception):
    print(Exception)

try:
    library_books = pd.read_csv('library_books.csv', encoding='utf-8')
    # 기본정보 확인
    print(library_books)
    # IT 분야 도서만 필터링해서 출력하세요
    print(library_books[library_books["분야"] == "IT"])
    # 가격이 30000원 이상인 도서들을 찾으세요
    print(library_books[library_books["가격"] >= 30000])
    # 분야별 평균 가격을 계산하세요
    print(library_books.groupby("분야")["가격"].mean())
except(Exception):
    print(Exception)
