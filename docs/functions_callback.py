## call by reference
## 나오는 값 처리
def add(first, second) :  # 호출 시 변수에 값이 할당됨
    sum = first + second 
    return sum # 상수 대신 변수 사용

def multiply(first, second) :  # 호출 시 변수에 값이 할당됨
    result = first * second 
    return result # 상수 대신 변수 사용

def process_call_function(first, second, callback_function):
    result = callback_function(first,second)
    return result

if __name__ == '__main__' :
    # result = add(5,6)
    result = process_call_function(5, 6, add)
    pass
    result = process_call_function(5, 6, multiply)
    pass