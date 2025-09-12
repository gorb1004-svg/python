# 함수선언(define)
def toaster(bread):
    print(f'{bread}이 구워지고 있다.')    #우리가 어떤 행동을 하고 있는데 우리는 볼수없음(ex. 심장이 뛰고 있는)
    return f'구워진 {bread}'

# 함수 사용
dish = toaster('식빵')
print(dish)