#-*-coding:utf8

# 클래스
# 기존 언어의 클래스와 기능은 동일함
# class 키워드를 사용하여 클래스를 선언함
# 클래스는 클래스 멤버로 클래스 변수와 클래스 메서드가 존재함
# 함수와 메서드는 동일한 기능과 개념을 가지고 있지만 클래스에 포함되어 있을 경우는 메서드라고 불리움

# 파이썬의 메서드는 기본적으로 사용하는 방법이 일반 함수와 동일함
# 파이썬의 메서드는 반드시 첫번째 매개변수로 self를 사용해야 함
# self는 내부적으로 사용하고 있기 때문에 메서드 사용 시 self 부분을 생략하고 입력
# 생성자를 사용자가 입력하지 않을 경우 자동으로 기본 생성자를 생성하여 사용함

# 클래스 선언 방법
# class 클래스명 :

# 클래스를 객체화 하는 방법
# 객체명 = 클래스명() / 괄호가 있는 것 : 생성자를 실행했다는 것

class Calculator: # 클래스 선언이 된 것
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

# Calculator의 생성자를 변수 cal1에 대입하여 Calculator 클래스를 객체화 시킴
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Service:
    secret = "영구는 배꼽이 두 개다"
    name2 = "" # 자바에서 초기화하는 방법 / # 기존 언어와 같은 방식으로 선언된 멤버 변수

    def setname(self, name): # self = 자기 자신을 의미
        # self.name 은 기존 언어에서 사용하는 방식과 다르게 멤버 변수로 선언됨
        # global name2 # 전역 변수를 안에서 사용할 수 있게 해줌 # 하지만 사용할 수 없음
        self.name = name
        # 기존 언어와 같은 방식으로 초기화된 멤버 변수 
        # self 키워드를 사용하지 않으면 클래스의 멤버 변수의 내용을 클래스의 메서드가 수정한 내용을 저정하지 못함
        self.name2 = name # 결국 self를 붙임 - 그래야 접근이 가능

    def sum(self, a, b): # 매개변수 3개!
        result = a + b
        print("{0}님 {1} + {2} = {3} 입니다.".format(self.name, a, b, result))
    # pass # 여기서 pass 는 클래스나 함수 등에 아무런 내용이 없을 경우 입력

pey = Service()
pey.setname("홍길동")
pey.sum(1, 1) # 매개변수 2개! # 함수와 메서드의 차이 / self는 내부적으로 존재하기 때문에 생략한다.

print("멤버 변수 name : {0}".format(pey.name))
# 기존 언어와 동일한 방식으로 사용한 멤버 변수
print("멤버 변수 name2 : {0}".format(pey.name2))

# __init__()
# __init__ 은 파이썬의 클래스 생성자 임
# 기존 언어의 생성자와 기능은 동일함
# 파이썬은 생성자의 이름을 고정해 놓음
# 각종 멤버 변수와 멤버 메서드를 초기화하는 것에 사용 됨
# 메서드와 동일하게 첫번째 매개변수는 self로 고정되어 있음
# 클래스를 객체화 시 실행되는 변수에 대입됨

print()
print("class Service2")
class Service2:
    # 클래스의 멤버 변수
    secret = "영구는 배꼽이 두 개다" # secret 는 멤버 변수임

    def __init__(self, name):
        self.name = name

    # self 키워드를 사용하지 않으면 클래스의 멤버 내에서 클래스의 멤버 변수에 접근이 불가능함
    def sum(self, a, b):
        result = a + b
        print("{0}님 {1} + {2} = {3} 입니다.".format(self.name, a, b, result))

pey2 = Service2("홍길동")
pey2.sum(1, 2)
print("영구의 배꼽은 몇 개? {0}".format(pey.secret))

pey2.secret = "영구의 배꼽은 사실 1개임" # self가 없다
print("영구의 배꼽은 몇 개? {0}".format(pey2.secret))

# 클래스를 사용하여 사칙연산 만들기
class FourCal:
    def setdata(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        # self.는 클래스의 멤버 변수에 접근하기 위해서 반드시 사용해야 함
        return self.a + self.b
        # return a + b # 초기화 되어있지 않은 변수끼리 합을 하는 것 - 오류 발생

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

a = FourCal()
print(type(a)) # 파이썬에서 지원하는 객체의 타입을 확인하는 명령어

a.setdata(4, 2)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

print()

# 3.xx 의 클래스 선언
class HousePark:
# 2.xx 의 클래스 선언
# class HousePark(object):

    # HousePark 클래스의 멤버 변수 lastName
    lastName = "박"

    # HousePark 클래스의 생성자
    # 클래스를 객체화하면서 동시에 멤버 변수 fullName을 선언하고 값을 초기화 함
    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, where):
        print("{0}, {1} 여행을 가다.".format(self.fullName, where))

    def love(self, other):
        print("{0}, {1} 사랑에 빠졌네".format(self.fullName, other.fullName))

    def fight(self, other):
        print("{0}, {1} 싸우네".format(self.fullName, other.fullName))

    # 연산자 오버로딩에 의해서 +, - 기호를 객체끼리의 연산에 사용할 수 있음
    def __add__(self, other):
        print("{0}, {1} 결혼했네".format(self.fullName, other.fullName))

    def __sub__(self, other):
        print("{0}, {1} 이혼했네".format(self.fullName, other.fullName))

pey = HousePark("응용")
pey.travel("태국")

# 클래스 상속
# 기존 언어와는 다르게 클래스명 뒤에 괄호를 사용하고 그 안에 상속할 클래스명을 입력함

# class 상속받을 클래스명(상속할 클래스명):

# HousePark 클래스를 상속 받은 클래스 HouseKim
class HouseKim(HousePark):
    # 상속 받은 멤버 변수 lastName의 값을 "김"으로 변경
    # 오버라이딩 됨
    lastName = "김"

    # 나머지 부분은 상속 받은 그대로 사용함

    # 클래스 HouseKim의 고유한 메서드 travelDay
    def travelDay(self, day):
        print("여행은 {0} 일간 입니다.".format(day))

    # 상속받은 메서드의 내용을 수정
    # 상속받은 메서드를 오버라이딩하여 사용

    def travel(self, where, day):
        print("{0}, {1} 여행 {2}일 가네".format(self.fullName, where, day))
        
        # 부모 클래스의 travel() 메서드 호출
        super().travel(where)
        # 2.x.x 버전에서는 super() 사용
        # super(자신의 클래스명, self).부모 클래스의 멤버
        # super(HouseKim, self).travel(where)

juliet = HouseKim("줄리엣")
juliet.travel("독도", 5)
juliet.travelDay(5)

# super() 는 클래스를 상속 받아 사용할 경우 부모 클래스의 멤버를 그대로 사용할 수 있는 명령어
# 상속받은 자식 클래스에서 부모의 클래스의 멤버를 호출

# super().부모 클래스의 멤버

# 연산자 오버로딩
# 연산자 오버로딩은 연산자(+, -, *, /)를 객체끼리의 연산에 사용할 수 있게 하는 기법
# + : __add__(매개변수)
# - : __sub__(매개변수)
# * : __mul__(매개변수)
# / : __truediv__(매개변수)

print()

pey = HousePark("응용")
juliet = HouseKim("줄리엣")

pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
# 연산자 오버로딩에 의해서 클래스의 멤버 메서드 __add__()가 실행됨
# 클래스명.__add__(클래스명2)의 형태가 아닌 클래스명1 + 클래스명2의 형태로 사용할 수 있음
pey + juliet
pey.fight(juliet)
pey - juliet
