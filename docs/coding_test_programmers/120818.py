# https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3

# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

# 10만원 이상 => 5프로, 30만원 이상 => 10프로, 50만원 이상 => 20프로

# price = 580000
# def solution(price):
#     if price >= 100000 :
#         sale = price * 0.05
#         answer = price - sale
#     elif price >= 300000 :
#         sale = price * 0.1
#         answer = price - sale
#     elif price >= 500000 :
#         sale = price * 0.2
#         answer = price - sale
#     return int(answer)
# print(solution(price))

## => 오답인 이유는 첫번째로 참인 조건이 실행되고 나머지는 무시된다. 따라서 10만원 이상인 모든 숫자들은 첫번째 조건에서 참이 되므로 첫번째 조건문만 실행되게 된다. 그러므로 할인율이 높은 조건을 먼저 검사하도록 코드를 작성해야 한다. 

price = 580000
def solution(price) :
    if price >= 500000 :
        sale = price * 0.2
        answer = price - sale
    elif price >= 300000 :
        sale = price * 0.1
        answer = price - sale
    elif price >= 100000 :
        sale = price * 0.05
        answer = price - sale
    else :
        answer = price
    return int(answer)
print(solution(price))