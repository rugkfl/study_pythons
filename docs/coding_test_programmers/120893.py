# https://school.programmers.co.kr/learn/courses/30/lessons/120893

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

my_string = "cccCCC"
print(my_string.swapcase())  #smapcase() => 대문자를 소문자로, 소문자를 대문자로 바꿔준다.
print()
# ----------------------------------

my_string = "cccCCC"
def solution(my_string):
    answer = my_string.swapcase()
    return answer
print(solution(my_string))