"""
날짜 : 2022/01/04
이름 : 강태호
내용 : 파이썬 기본 입출력
"""

name = input("이름 입력: ")
age = input("나이 입력: ")

year = 2021 - int(age)
year = str(year)

print(name+'님은 '+age+'세이고, '+year+'년도에 태어났습니다.')