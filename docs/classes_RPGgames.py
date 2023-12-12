# function만 사용해 적 캐릭터 만들기
# first 적 캐릭터
name = "first"
health_first = 120
damage = 0

def attack(health, damage) :
    health = health - damage
    return health

damage_first = attack(health_first, 5)

# second 적 캐릭터
name = "second"
health_second = 200
damage = 0

damage_second = attack(health_second, 10)

# function만 사용 시 제한 극복 -> class
# self는 function과 function 사이를 소통하게 해주는 존재

class Enemy :
    def __init__(self, name, health) : #생성자 / Enemy = self = self / self = class / 여기서의 name 외부에서 들어오는 name
        self.name = name      # 외부 변수 name 값이 내부 변수(self.name)에 할당 / 여기서의 name은 class의 name
        self.health = health
        self.damage = 0  # 내부변수
        pass

    def attack(self, damage) :
        self.health = self.health - damage #외부변수
        return self.health
    
    def function_name(self) : # self 키워드 필요(class 소속 확인용)
        pass
        return 0
    
# first_enemy = Enemy()  # 자신의 자원(function과 variables) 확인
first_enemy = Enemy('first', 150)  # 각각 다른 그릇에 담김 => 하지만 같은 class안에서 파생
second_enemy = Enemy('second', 300)  # 각각 다른 그릇에 담김 => 하지만 같은 class안에서 파생
pass
    
    