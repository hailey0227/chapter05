#-*-coding:utf8

# 클래스나 변수 등을 포함한 모듈

PI = 3.141592

# 2.XX 방식
# class Math(object):
class Math:
    def solv(self, r):
        return PI * (r ** 2)
    
def sum(a, b):
    return a + b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))