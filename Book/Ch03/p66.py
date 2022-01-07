# 무한 루프 (loop)
numData = []      # 빈 리스트

while True :
    num = int(input("숫자 입력 : "))

    if num % 10 == 0 :      # exit 조건식
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)    # list 추가

