# 가로 * 세로 * 높이 = 직육면체
# input : 가로 세로 높이
# output : 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3

str_input = input("가로 세로 높이 :")
str_first, str_second, str_third = "4 1 1".split()
num_first, num_second, num_third = int(str_first), int(str_second), int(str_third)
print("가로({})m * 세로({})m * 높이({})m = 직육면체(4)m^3".format(num_first, num_second, num_third))


