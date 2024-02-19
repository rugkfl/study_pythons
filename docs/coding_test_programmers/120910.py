# https://school.programmers.co.kr/learn/courses/30/lessons/120910

# 문제 설명
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

n = 2     # 세균 수
t = 10    # 경과한 시간
def solution(n, t):
    answer = ((2**t)*n)
    return answer
print(solution(n, t))

# 시간에 따라 2배로 증가하는 세균 수를 거듭제곱으로 구한 값에 처음 세균의 수를 곱해준다
# print((2**15)*7)