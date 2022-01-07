# (1) 카운터와 누적변수
cnt = tot = 0   #변수초기화
while cnt < 5 :   # True : loop 수행
    cnt += 1   #카운터 변수(cnt = cnt + 1)
    tot += cnt   #누적변수 : tot = tot + cnt
    print(cnt, tot)

# 실습 1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []    #빈 리스트

while cnt < 100 :    # 100회 반복
    cnt += 1   # 카운터
    if cnt % 3 == 0 :
        tot += cnt    #누적변수
        dataset.append(cnt)    #cnt추가

print('1 ~ 100 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)
