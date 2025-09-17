class Car:                          #> 자동차라는 설계도(class)
    gear = 0                        #> 기어는 0단
    on = False                      #> 시동은 꺼짐

#> class는 이용시 객체화(사람/물건)을 만들기 때문에 생성자는 필수다.
#> 그런데 프로그래밍의 규칙중 하나는 너무 당연하게 있어야할 것들을 생략이 가능하다.
#> 생성자는 __init__
    def __init__(self):
#> 혹시나 기어가 들어가 있거나 시동이 켜있을수 있어 초기 상태로 되돌려 놓는다.
        self.gear = 0
        self.on = False

#> 멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체를 알기하기 위한 self를 기본으로 가지고 있는다.
    def start(self):
        if self.on == False:        #> 현재 자동차 시동상태(self.on)가 꺼져(False) 있으면
            print('시동이 걸렸습니다.')
            self.on = True
        else:
            print('시동이 이미 걸려있습니다.')

    def change(self, gear):
        print(f'{gear} 단으로 변속 했습니다.')
        self.gear += gear

#> car 클래스를 객체화(복사)
#> 객체를 통해 사용하고 싶은 멤버 호출
car = Car()

#시동 걸기
car.start()
#변속하기
car.change(5)
print(f'현재 car의 gear 단수: {car.gear}')















