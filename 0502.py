#-*-coding:utf8

# 모듈(다른 언어의 라이브러리)
# 클래스, 함수, 변수 등을 미리 만들어두고 필요할 때 가져다 사용할 수 있도록 모아놓은 파일
# 기본 조건 : 실행하는 파일과 모듈이 같은 폴더에 존재해야함

# 사용 이유
# 모듈을 사용하는 이유는 유지보수가 편함
# 다른 사람과의 협업이 가능함
# 모듈 사용 시 사용법만 알고 있으면, 해당 모듈의 내부 구조를 몰라도 사용이 가능함
# 모듈을 가장 잘 보여주는 것 = 자동차 : 엄청난 수의 모듈들로 구성되어있다.

# 사용방법
# import 모듈명
# 모듈 사용 시 해당 모듈명과 클래스, 함수, 변수 등을 모듈명.멤버로 사용해야 함
# mod.sum()

# from 모듈명 import 모듈 함수
# 모듈 사용 시 해당 모듈의 클래스, 함수, 변수 등을 모듈명 없이 사용할 수 있음
# sum()

# import mod1
# print("mod1 모듈의 sum 함수 사용 : {0}".format(mod1.sum(3, 4)))

# print()

# print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(3, 4)))
# print("mod1의 safe_sum 함수 사용 : {0}".format(mod1.safe_sum(1, "a")))

# from 절을 사용하여 mod1의 sum, safe_num을 모두 불러와 사용하기 때문에 mod1을 붙여서 사용하면 오히려 오류가 발생함
from mod1 import sum, safe_sum

print("mod1 모듈의 sum 함수 사용 : {0}".format(sum(3, 4))) # mod1을 붙이면 오류가 난다.

# 문제 1) 사칙연산을 위한 계산기 프로그램을 모듈을 활용한 방식으로 제작하세요
# 모듈명 : Cal
# 사칙연산 함수명 plus, minus, multi, divide
# 각각 함수는 매개 변수를 2개씩 가지고 있음(first, second)

import Cal

print("Cal 모듈 plus 함수 사용 : {0}".format(Cal.plus(4, 2)))
print("Cal 모듈 minus 함수 사용 : {0}".format(Cal.minus(4, 2)))
print("Cal 모듈 multi 함수 사용 : {0}".format(Cal.multi(4, 2)))
print("Cal 모듈 divide 함수 사용 : {0}".format(Cal.divide(4, 2)))




from Cal2 import plus, minus, multi, divide

# a.Cal2(4, 2)
# print(a.plus())
# print(a.minus())
# print(a.multi())
# print(a.divide())

print("Cal2 모듈 plus 함수 사용 : {0}".format(plus(4, 2)))
print("Cal2 모듈 minus 함수 사용 : {0}".format(minus(4, 2)))
print("Cal2 모듈 multi 함수 사용 : {0}".format(multi(4, 2)))
print("Cal2 모듈 divide 함수 사용 : {0}".format(divide(4, 2)))