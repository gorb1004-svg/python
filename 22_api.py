#api Application Programming Interface
 # 인터페이스 = 스위치같은, 브레이크같은 거라고 생각하면 됌
 # 프로그램과 프로그램이 대화할 수 있게 도와주는 ‘메뉴판’ 같은 것
 # API = 프로그램끼리 정보를 주고받는 통로

def print_max(x,y):
    '''
    입력된x 와 y 중 큰 값을 알려주는 함수입니다.

    :param x: 인자값1
    :param y: 인자값2
    '''

    print(f'{x} 와 {y} 중에...');
    if x > y:
        print(f'{x} 가 더 큽니다.')
    else:
        print(f'{y} 가 더 큽니다.')

print_max(5, 10)
# 해당 함수에 대한 출력
print(f'함수설명: {print_max.__doc__}')