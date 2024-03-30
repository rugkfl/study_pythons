num_list = [1, 2, 3, 4, 5]
def solution(num_list):
    back_list = []
    for i in reversed(num_list) : # 리스트의 값을 역순으로 해주는 함수
        back_list.append(i)
    answer = back_list
    return answer
print(solution(num_list))