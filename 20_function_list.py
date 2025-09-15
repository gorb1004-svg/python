# 반환타입: O 매개변수: O / 토스트기
def toaster(bread):                          # def은 선언문이고 토스트기가 함수이름임.(지금 함수를 만들거야. 함수명은 토스트기야) / 브래드는 매개변수이다.
    print(f'{bread}이 들어간다.')              # 즉, “이(토스트기) 함수는 어떤 값을 하나 받아올 건데, 그걸 함수 안에서는 브래드라는 이름으로 부를 거야” 라는 뜻.
    return f'툭 튀어나오는 {bread}'

dish = toaster('식빵')
print(dish)

# 반환타입: O 매개변수: X / 수도꼭지
def faucet():
    return f'흐르는 물'
print(faucet())


def faucet():
    return f'물'
print(faucet())


# 반환타입: X 매개변수: O / 쓰레기
def garbage(쓰레기):
    print(f'{쓰레기}가 들어간다.')
garbage('깡통쓰레기')


# 반환타입: X 매개변수: X / 온도계
def thermometer():
    print(f'온도는 27도입니다')
thermometer()