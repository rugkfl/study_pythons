array = [149, 180, 192, 170]
# array = [180, 120, 140]
height = 167
def solution(array, height) :
    count = 0 # 초기화
    for i in range(len(array)) :
        if height < array[i] :
            count += 1
        else :
            continue # 조건을 충족하지 않는 경우 다시 조건절 시작으로 감
    answer = count
    return answer 
print(solution(array, height))
