# n = 7
# def solution(n):
#     if n % 7 == 0 :
#         print(n // 7)
#     answer = 0
#     return answer

n = 7
def solution(n):
    if n % 7 == 0 :
        whole_pizza = n//7
    elif n % 7 != 0 :
        whole_pizza = (n // 7) + 1
    answer = whole_pizza
    return answer
print(solution(n))