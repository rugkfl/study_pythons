# https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 문제 설명
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
def solution(s1, s2):
    same_list = list(set(s1) & set(s2))
    answer = len(same_list)
    return answer
print(solution(s1, s2))

# s1 = ["a", "b", "c"]
# s2 = ["com", "b", "d", "p", "c"]
# same_list = list(set(s1) & set(s2))
# answer = len(same_list)
# print(answer)

## 해설
### 두개의 리스트를 비교해서 교집합인 값의 개수를 출력하는 문제이므로 리스트끼리 비교할때 set() 함수를 사용할 수 있다. 
### set(리스트) => 리스트의 중복 제거
### set(리스트 1) & set(리스트 2) => 교집합의 값만 출력
### set(리스트 1) | set(리스트 2) => 합집합의 값만 출력
### set(리스트 1) - set(리스트 2) => 차집합의 값만 출력(or set(리스트 2) - set(리스트 1))
### set(리스트 1) ^ set(리스트 2) => 대칭 차집합 값만 출력(= 두 리스트에서 겹치는 값을 제외한 '모든 값'을 구할때)