while True :
    try :
        a, b, c = input("숫자 3개를 입력 : ") # 숫자 3개 입력
        answer_list = [a, b, c]
        num_try = int(input("도전 횟수 입력 : ")) # 도전 횟수
        for i in range(num_try):
            chance_first, chance_second, chance_third = input("숫자 입력 : ") # 맞추는 기회
            str_chance = [chance_first, chance_second, chance_third]
            pass

            count_strike = 0 #스트라이크 갯수
            count_ball = 0 #볼 갯수
            for x in range(len(str_chance)) :
                if str_chance[x] == answer_list[x] :
                    count_strike = count_strike + 1
                elif str_chance[x] != answer_list[x] and str_chance[x] in answer_list:
                    count_ball = count_ball + 1

            if count_strike == 0 and count_ball == 0 :
                print("아웃")
            elif count_strike == 3 and count_ball == 0 :
                break # 이 조건이 참일 시 break되어 for루프를 빠져나오고 밑에 있는 if절로 가게됨
            else :
                print("{}S {}B".format(count_strike, count_ball))
        if count_strike == 3 and count_ball == 0: # while루프를 해당 조건을 통해 완전히 종료시키기 위해서는 while 루프 내에 해당 조건이 위치되어야 함.
            print("프로그램 종료")
            break
    except :
            print("입력 양식이 잘못되었습니다.")
            pass
    
            
    
 

# 선택 사항)
# - 3S가 나올 경우 프로그램 종료 v
# - 입력 양식이 틀릴 경우 다시 입력 => try-except v
# - 숫자 3개 입력 시 값 중에 똑같은 값이 있을 경우 다시 입력

