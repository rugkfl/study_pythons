numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def solution(numbers):
    sum_numbers = sum(numbers)
    len_numbers = len(numbers)
    answer = sum_numbers / len_numbers
    return answer
print(solution(numbers))