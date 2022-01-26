#(1) 함수 정의
def calc_func(a, b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

#(2) 함수 호출
p, m = calc_func(10, 20)
print('plus = ', p())
print('minus= ', m())

#(3) 클래스 정의
class calc_class :
    x = y = 0

    #생성자
    def __init__(self, a, b):
        self.x = a
        self.y = b

    #클래스 함수
    def plus(self):
        p = self.x + self.y
        return p
    #클래스 함수
    def minus(self):
        m = self.x - self.y
        return m

#(4) 객체 생성
obj = calc_class(10, 20)

#(5) 멤버 호출
print('plus = ', obj.plus())
print('minus = ', obj.minus())
