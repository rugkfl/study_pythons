# Class 초기화 방법
dict_initial = {}       # empty
dict_initial = dict()    # empty

list_car_infor = ['Ford', 'Mustang', 1964]

# key(str) : value(여러 변수 종류 가능) 
dict_carinfor = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "items" : []
}
model = dict_carinfor["model"]
print("dict_carinfor 있는 model name : {}".format(model))

# key로 인한 값 변경
dict_carinfor['year'] = 1970
# 새로운 key와 값 정의
dict_carinfor['color'] = "red"
dict_carinfor['color'] = ["red," "yellow", "brown"]


pass


# list는 index로 접근
# dict은 key로 접근