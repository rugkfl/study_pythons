numbers = [1, 2, 3, 4, 5]
num1 = 1
num2 = 3
def solution(numbers, num1, num2):
    answer = numbers[num1 : num2 + 1]
    return answer
print(solution(numbers, num1, num2))

# numbers = [1, 2, 3, 4, 5]
# num1 = 1
# num2 = 3
# print(numbers[num1 : num2+1])