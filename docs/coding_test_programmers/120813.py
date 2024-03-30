# https://school.programmers.co.kr/learn/courses/30/lessons/120813

# 문제 설명
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

# n = 15 
# num = 0
# num_list = []
# result_list = []
# for i in range(n) :
#     num += 1
#     num_list.append(num)
# for i in range(len(num_list)) :
#     if num_list[i] % 2 != 0 :
#         result_list.append(num_list[i])
# print(result_list)


n = 10
def solution(n):
    num = 0
    num_list = []
    result_list = []
    for i in range(n) :
        num += 1
        num_list.append(num)
    for i in range(len(num_list)) :
        if num_list[i] % 2 != 0 :
            result_list.append(num_list[i])
    return result_list
print(solution(n))