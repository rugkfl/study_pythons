# https://school.programmers.co.kr/learn/courses/30/lessons/120839?language=python3

# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

## 딕셔너리는 key : value의 쌍으로 데이터를 저장하는 자료형
## 중괄호{} 안에 콜론(:)으로 구분된 키와 값의 쌍을 나열하여 생성
## 값을 꺼내는 방법은 1. key값 활용 2. get() 메소드 사용
## join : 문자열 리스트를 하나의 문자열로 결합할 때 사용 
## 문자열의 각 요소 사이에 지정된 구분자를 삽입하여 그 결과를 반환


rsp = "205"
rsp_dict = {'2' : '0', '0' : '5', '5' : '2'}
print(''.join([rsp_dict[i] for i in rsp]))

rsp = "205"
for i in rsp :
    answer = rsp_dict[i]
    print(answer, end='')
print()


rsp = "205"
def solution(rsp):
    rsp_dict = {'2' : '0', '0' : '5', '5' : '2'}
    answer = ''.join(rsp_dict[i] for i in rsp)
    return answer
print(solution(rsp))

