# 사용자 입력 반복 곱셈 계산기
# 'q' 입력 시 종료
# 최소 function 2개 사용

# funtion -> while -> q

# 곱셈 계산기
def multiply(num_first, num_second) :  
    multiply_result = num_first * num_second
    return multiply

input_q_sign =""

input_q_sign = input("종료 코드 : ")
if input_q_sign == 'q' :
    print("프로그램 종료")

while input_q_sign != 'q' :
    try:
        call_first = int(input("단 수 입력 : "))
        call_second = int(input("숫자 입력 : "))
        print("곱셈 결과 :{} * {} = {}".format(call_first, call_second, call_first*call_second))
    except ValueError:
        print("프로그램 종료")  
        break

    




    










