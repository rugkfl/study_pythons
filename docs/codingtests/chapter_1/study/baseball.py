# 초기화
ball_count = 0
strike_count = 0


# while True :
    # try :

a, b, c = input("숫자 3개를 입력 : ") # 숫자 3개 입력
answer_list = [a, b, c]
num_try = int(input("도전 횟수 입력 : ")) # 도전 횟수
for i in range(num_try):
    chance_first, chance_second, chance_third = input("숫자 입력 : ") # 맞추는 기회
    str_chance = [chance_first, chance_second, chance_third]
    pass
    
    for x in range(len(str_chance)) :
        if str_chance[x] == answer_list[x] :
                print("스트라이크")
        elif str_chance[x] != answer_list[x] in answer_list :
                print("볼")
        else :
            print("아웃")




                    
# if a,b,c ==숫자 and a,b,c !=위치
    # print("볼")
# elif  a,b,c ==숫자 and a,b,c ==위치
    # print("스트라이크")
# else  a,b,c !=숫자 and a,b,c !=위치
    # print("아웃")

# 선택 사항)
# - 3S가 나올 경우 프로그램 종료
# - 입력 양식이 틀릴 경우 다시 입력 => try-except
# - 숫자 3개 입력 시 값 중에 똑같은 값이 있을 경우 다시 입력

