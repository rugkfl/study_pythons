# # https://school.programmers.co.kr/learn/courses/30/lessons/120819

# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

money = 5500
def solution(money) :
    return[money // 5500, money % 5500]
print(solution(money))

# => money % 5500 = money - (5500 * 2) 이렇게 해야 나머지 값이 나옴

# money = 5000
# def solution(money):
#     americano = 5500   # 아메리카노 한잔 가격
#     count_coffee = 0   # 마실 수 있는 커피의 잔 수
#     change = 0         # 잔돈 
#     answer = []
#     if money % americano == 0 :
#         count_coffee += 1
#         answer.append(count_coffee)
#         answer.append(change)
#     elif money % americano != 0 & money != americano :
#         count_coffee = money // americano
#         change = money - (americano * count_coffee)
#         pass
#         answer.append(count_coffee)
#         answer.append(change)
#     return answer
# print(solution(money))



# money = 5500       # 현재 소지한 금액
# americano = 5500   # 아메리카노 한잔 가격
# count_coffee = 0   # 마실 수 있는 커피의 잔 수
# change = 0         # 잔돈 
# result_list = []
# if money % americano == 0 :
#     count_coffee += 1
#     result_list.append(count_coffee)
#     result_list.append(change)
# elif money % americano != 0 & money != americano :
#     count_coffee = money // americano
#     change = money - (americano * count_coffee)
#     pass
#     result_list.append(count_coffee)
#     result_list.append(change)
# print(result_list)