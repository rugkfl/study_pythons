# https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.



# (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1)


n = 20
def solution(n) :
    num_list = []
    for i in range(1, n+1) :
        if n % i == 0 :
            num_list.append(i)
    result = len(num_list)
    return result
print(solution(n))

