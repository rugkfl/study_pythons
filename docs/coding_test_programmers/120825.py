# https://school.programmers.co.kr/learn/courses/30/lessons/120825

# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.


# my_string = 'hello'
# n = 3
# for i in range(len(my_string)) :
#     answer = my_string[i] * n
#     print(answer, end='')

my_string = 'hello'
n = 3
def solution(my_string, n) :
    answer = ''  # function을 이용할 경우 end=''을 대신하여 초기화 값에 반복해서 추가해주고 그 변수명을 return 시켜야 함
    for i in range(len(my_string)) :
        answer += my_string[i] * n
    return answer
print(solution(my_string, n))