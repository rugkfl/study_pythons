my_string = '"jaron"'
def solution(my_string):
    answer = my_string[:: -1]
    return answer
print(solution(my_string))

# my_string = "jaron"
# print(my_string[:: -1]) # 거꾸로 출력됨