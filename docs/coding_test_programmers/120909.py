# https://school.programmers.co.kr/learn/courses/30/lessons/120909

# 문제 설명
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

## 144 ** 0.5를 해주면 제곱근을 알 수 있다
## int(n**0.5) ** 2 == n => 0.5를 제곱해서 구한 제곱근에다가 다시 2를 제곱해주면 정수의 제곱수를 알 수 있고 그 제곱수가 n이랑 같은지를 확인하여 제곱수인지 아닌지를 판별한다.  

# n = 144
# if int(n**0.5) ** 2 == n:
#     answer = 1
# else :
#     answer = 2
# print(answer)

n = 144
def solution(n):
    if int(n**0.5) ** 2 == n :
        answer = 1
    else :
        answer = 2
    return answer
print(solution(n))