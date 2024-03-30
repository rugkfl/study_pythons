n = 10
def solution(n):
    n_list = []
    for i in range(n) :
        i += 1
        if i % 2 == 0:
            n_list.append(i)
    answer = sum(n_list)
    return answer
print(solution(n))