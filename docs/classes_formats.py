# class basic format
# 1. import(같은 파일에 있을 경우 생략)
# 2. class instance : 생성자 호출
# 3. call function : 원하는 기능
class Class_name :
    def __init__(self) : #생성자
        pass
    def function_name(self) : # self 키워드 필요(class 소속 확인용)
        pass
        return 0
    
class Person :
    def add_age(self) : 
        pass
        print("45세")
        return 0
## 1. import(같은 파일에 있을 경우 생략)
# 같은 파일이므로 생략
## 2. class instance
person = Person()
# 3. call function
person.add_age()

# 사칙연산 되는 class 작성
# 덧셈, 뺄셈
class Arithmetics :
    def __init__(self) : #생성자(class가 갖고 있는 자원)
        pass

    def add(self, first, second) :   # 호출 시 변수에 값이 할당됨
        sum = first + second 
        return sum # 상수 대신 변수 사용

    def minus(self, first, second) :
        result = first - second  
        return result

# 1. import(같은 파일에 있을 경우 생략)
# 2. class instance
arithmetics = Arithmetics()
# 3. call function
print(arithmetics.add(5, 6))
pass
