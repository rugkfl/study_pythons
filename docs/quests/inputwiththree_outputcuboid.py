# 가로 * 세로 * 높이 = 직육면체
# input : 가로 세로 높이
# output : 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3


str_first, str_second, str_third = input().split()
first = int(str_first)
second = int(str_second)
third = int(str_third)
cuboid = first * second * third
print("가로({})m * 세로({})m * 높이({})m = 직육면체({})m^3".format(first, second, third, cuboid))


