n = 10 
def solution(n) :
    n_list = []
    for i in range(n) :
        i += 2
        n_list.append(i)
    return n_list
print(solution(n))