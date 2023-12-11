class Arithmetics :
    def __init__(self) : 
        pass

    def minus(self, first, second) :
        result = first - second  
        return result
    
    def multiply(self, first, second) :
        result = first * second
        return result

    def divide(self, first, second) :
        result = first / second
        return result
    
num_first, num_second = map(int, input().split())
arithmetics = Arithmetics()
print("{}".format(arithmetics.minus(num_first, num_second)))
print("{}".format(arithmetics.multiply(num_first, num_second)))
print("{}".format(arithmetics.divide(num_first, num_second)))



pass