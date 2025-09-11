import random
from operator import truediv

# 술게임 업앤다운이라고 생각됨(횟수지정 없음)

number = random.randint(1, 31) ##1-31까지 가상의 namber에 랜덤한 숫자 받기
print(f' 내 마음속 숫자:{number}') ## 출력해, 내마음속 숫자 문장과, 랜덤 숫자를!
running = True ## while의 실행조건이 running 이고, 시작은 true로 while문을 실행시킴

####### 와일문이 어떻게 멈추고 돌아갔는지 확인해보라고?


while running: ##while 종료 횟수가 정해지지 않을 때 까지 무한 반복함.
    # 입력받은 값을 정수(int)로 변환하여 guess에 대입
    guess = int(input('1~31중 내가 생각한 숫자는?')) ## guess가 계속 입력을 받아야하는 이유는, 정답을 맞추기 위해서.
    print(f'입력받은 숫자:{guess}') ## 내가 생각한 입력받은 숫자가 정답 기준으로 크다/작다/정답으로 표현됨

    if number == guess: ## 넘버랑 게스랑 정답이 같아서 실행을 중단하겠다. false
        print('정답입니다.')
        running = False
    if number > guess: ##넘버가 게스보다 크다. / while 처음으로 돌아가서 guess 값을 받는다
        print('내가 생각한 숫자보다 작습니다.')
    if number < guess: ##넘버가 게스보다 작다 / while 처음으로 돌아가서 guess 값을 받는다
        print('내가 생각한 숫자보다 큽니다.')








#    pass
