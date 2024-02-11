numbers = [1, 2, 3, 4, 5]
def solution(numbers):
    a = max(numbers)
    b = sorted(numbers, reverse=True)[1]
    answer = a * b
    return answer
print(solution(numbers))

# numbers = [1, 2, 3, 4, 5]
# # numbers = [0, 31, 24, 10, 1, 9]	
# a = max(numbers)
# b = sorted(numbers, reverse=True)[1] #sorted는 정렬을 해주고 reverse를 사용하면 내림차순이 됨/인덱스로 두번째로 큰 수를 찾음
# answer = a * b
# print(answer)