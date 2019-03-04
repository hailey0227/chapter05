#-*-coding:utf8

def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
        return result

# 모듈의 테스트
# 제작한 모듈이 정상적으로 동작하는지 확인하는 구문
# 현재 실행한 파일이 실제 실행한 파일인지 아니면 import된 파일인지 확인하는 구문

# 파이썬의 실행 시작 지점 - 하지만 우리는 지정한 적 없다.
# python 파이썬 코드 파일을 하면 자동으로 main문이 생성됨 / 자바에서 main 과 같음
# if __name__ == "__main__": 를 이용하면 현재의 모듈이 정상적으로 

if __name__ == "__main__":
    print(safe_sum("a", 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))