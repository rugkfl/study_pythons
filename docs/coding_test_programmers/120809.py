numbers = [1, 2, 3, 4, 5]
def solution(numbers):
    numbers_list = []
    for i in range(len(numbers)) :
        result = numbers[i] * 2
        numbers_list.append(result)
    answer = numbers_list
    return answer
print(solution(numbers))

# numbers = [1, 2, 3, 4, 5]
# numbers_list = []
# for i in range(len(numbers)) :
#     result = numbers[i] * 2
#     numbers_list.append(result)
# print(numbers_list)