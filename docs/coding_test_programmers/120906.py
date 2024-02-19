# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 문제 설명
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# n = 1234
# n_str = str(n)
# str_list = []
# for i in range(len(n_str)) :
#     str_list.append(n_str[i])
# int_list = list(map(int, str_list))  # 문자열을 정수로 바꿀 때 사용 
# print(sum(int_list))

n = 1234
def solution(n):
    n_str = str(n)
    str_list = []
    for i in range(len(n_str)) :
        str_list.append(n_str[i])
    int_list = list(map(int, str_list))
    answer = sum(int_list)  
    return answer
print(solution(n))