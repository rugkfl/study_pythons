# # https://school.programmers.co.kr/learn/courses/30/lessons/120905

# 문제 설명
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
multiple_list = []
for i in range(len(numlist)) :
    if numlist[i] % n == 0 :
        multiple_list.append(i)
    else :
        continue
result = [numlist[i] for i in multiple_list]  
# multiple_list의 값들인 2, 5, 8이라는 인덱스를 가진 numlist의 값들인 6, 9, 12를 result에 저장하고 출력 가능
print(result)


n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
def solution(n, numlist):
    multiple_list = []
    for i in range(len(numlist)) :
        if numlist[i] % n == 0 :
            multiple_list.append(i)
        else :
            continue
    answer = [numlist[i] for i in multiple_list]
    return answer
print(solution(n, numlist))