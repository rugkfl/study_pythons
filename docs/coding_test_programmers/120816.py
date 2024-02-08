slice = 7
n = 10

def solution(slice, n):
    if n % slice == 0 :
        result = n // slice
    elif n % slice != 0 :
        result = (n // slice) + 1
    answer = result
    return answer
print(solution(slice, n))



# if n % slice == 0 :
#     answer = n // slice
# elif n % slice != 0 :
#     answer = (n // slice) + 1
# print(answer)