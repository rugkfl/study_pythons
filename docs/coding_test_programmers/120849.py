# https://school.programmers.co.kr/learn/courses/30/lessons/120849

# 문제 설명
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# my_string = "bus"
# vowels = ['a', 'e', 'i', 'o', 'u']
# for i in range(len(vowels)) :
#     my_string = my_string.replace(vowels[i], '')
# print(my_string)

my_string = "nice to meet you"
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vowels)) :
        my_string = my_string.replace(vowels[i], '')  # 특정문자열 제거 => replace()
    return my_string
print(solution(my_string))