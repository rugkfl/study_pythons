n = 10
k = 3
def solution(n, k):
    service = 0
    result = 0
    if n < 10 and k > 0 :
        result = (n * 12000) + (k * 2000)
    elif n >= 10 and k > 0 :
        service = n // 10
        result = (n * 12000) + ((k * 2000) - (service * 2000))
    answer = result
    return answer
print(solution(n, k))


# n = 10 # 양꼬치 n인분(양꼬치 1인분 12,000/ 10인분 먹으면 음료수 1개 서비스)
# k = 3 # 음료수 개수(음료수 개당 2,000) 
# service = 0
# result = 0
# if n < 10 and k > 0 :
#     result = (n * 12000) + (k * 2000)
   
# elif n >= 10  and k > 0 :
#     service = n // 10 
#     result = (n * 12000) + ((k * 2000) - (service * 2000))
   
# print(result)