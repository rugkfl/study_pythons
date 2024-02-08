num_list = [1, 2, 3, 4, 5]
def solution(num_list):
    even_list = []
    odd_list = []
    count_list = []
    for i in range(len(num_list)) :
        if num_list[i] % 2 == 0 :
            even_list.append(num_list[i])
        elif num_list[i] % 2 != 0 :
            odd_list.append(num_list[i])
    result_1 = len(even_list)
    result_2 = len(odd_list)
    count_list.append(result_1)
    count_list.append(result_2)
    answer = count_list
    return answer
print(solution(num_list))

# num_list = [1, 2, 3, 4, 5]
# # num_list = [1, 3, 5, 7]
# even_list = []
# odd_list = []
# count_list = []
# for i in range(len(num_list)) :
#     if num_list[i] % 2 == 0 :
#         even_list.append(num_list[i])
#     elif num_list[i] % 2 != 0 :
#         odd_list.append(num_list[i])
# result_1 = len(even_list)
# result_2 = len(odd_list)
# count_list.append(result_1)
# count_list.append(result_2)
# print(count_list)