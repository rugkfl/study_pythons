# # https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.


my_string = '"BCBdbe"'
letter = "B"
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer
print(solution(my_string, letter))

# replace : 특정 문자열 제거 혹은 교체
# 변수명.replace('제거하고자 하는 문자열', '') => 해당 문자열 제거
# 변수명.replace('교체하고자 하는 문자열', '새로 사용하고 싶은 부분문자열') => 해당 문자열 교체
# 변수명.replace('제거하고자 하는 문자열', '', 2) => 2는 두번 삭제하라는 의미