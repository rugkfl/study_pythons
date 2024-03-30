# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# my_string = "1a2b3c4d123"
# num_list = []
# for i in my_string :
#     try :  # 반복문을 통해 int로 변환이 가능한 문자열만 리스트에 append
#         int(i)
#         num_list.append(i)
#     except :  # 에러가 나면 통과해서 다시 처음으로
#         continue
# int_list = list(map(int, num_list))  # list의 문자열을 int로 바꿔줌
# result = sum(int_list)
# print(result)


# my_string = "1a2b3c4d123"
my_string = "aAb1B2cC34oOp"
def solution(my_string):
    num_list = []
    for i in my_string :
        try :
            int(i)
            num_list.append(i)
        except :
            continue
    int_list = list(map(int, num_list))
    answer = sum(int_list)
    return answer
print(solution(my_string))