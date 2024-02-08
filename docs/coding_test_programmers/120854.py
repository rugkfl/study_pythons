strlist = ["We", "are", "the", "world!"]
def solution(strlist):
    len_list = []
    for i in range(len(strlist)) :
        len_list.append(len(strlist[i]))
    answer = len_list
    return answer
print(solution(strlist))

# strlist = ["We", "are", "the", "world!"]
# len_list = []
# for i in range(len(strlist)) :
#     len_list.append(len(strlist[i]))
# print(len_list)