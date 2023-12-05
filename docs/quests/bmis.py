# input(두 값은 정수) : 몸무게, 키 
# BMI = 몸무게(kg) / 키(m)^2 
#  분류
# 18 미만 : 저체중
# 18 - 22 : 정상
# 23 - 24 : 과체중
# 25 이상 : 비만

str_weight = input("몸무게 : ")
str_height = input("키 :")
first_kg = int(str_weight)
second_cm = int(str_height)
print("{}".format(first_kg))
print("{}".format(second_cm))

bmi = int(first_kg / (second_cm/100)**2)
print("{}".format(bmi))

if bmi < 18 :
    pass
    input("{}은 18미만이므로 저체중입니다.".format(bmi))
elif bmi < 23 :
    pass
    input("{}은 23미만이므로 정상입니다.".format(bmi))
elif bmi < 25 :
    pass
    input("{}은 25미만이므로 과체중입니다.".format(bmi))
else :
    pass
    input("{}은 25이상이므로 비만입니다.".format(bmi))