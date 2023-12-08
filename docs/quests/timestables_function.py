def multiply(num_first, num_second) :
    multiply_result = num_first * num_second

    return multiply_result



while True :   # 무한루프
    try :
        str_input = input("단 수 입력 : ")  # q라는 문자열을 받아야 하므로 input
        num_first = int(str_input)      # num_first는 단수인 숫자를 받아야하므로 int
        if num_first == 30 or num_first == 35 or num_first == 20 : # 가정
            for num_second in range(1,10) :   # 반복 / range : 특정 구간의 숫자의 범위를 만들어주는 함수(미만개념)
                print("{} * {} = {}".format(num_first, num_second, multiply(num_first, num_second)))  # multiply(num_first, num_second) => num_fisrt와 num_second에 숫자가 지정이 되면 multiply_result = num_first * num_second 된 값을 return 해준다
                pass
            pass
        else :
            print("30, 35, 20이 아닌 숫자를 입력하였습니다. \n다시 입력해주세요.")  # \n => enter 키
    except :
        if str_input == "q" :
            print("프로그램 종료")
            break
        else :
            print("30, 35, 20이 아닌 문자를 입력하였습니다. \n다시 입력해주세요.")
            pass

 
    




