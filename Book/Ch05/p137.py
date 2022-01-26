# (1) 중첩함수 정의
def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val   #nonlocal 명령어
        num_val = value

    return getter, setter   #함수 클로저 반환

# (2) 외부 함수 호출
getter, setter = main_func(100)   #num 생성

# (3) 획득자 호출
print('num = ', getter())   # 획득한 num 확인

# (4) 지정자 획득
setter(200)
print('num = ', getter())