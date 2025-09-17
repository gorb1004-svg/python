# 이 코드는 리스트 안에 있는 특정 값(3)의 위치(인덱스)를 전부 찾아내기 위해 작성된 거예요.
# 왜 이렇게 해야 하냐?
# 리스트 안에서 특정 값의 모든 위치를 찾아내려면, 이렇게 무한 반복 + 인덱스 이동 + 예외 처리를 조합해야 가능하기 때문이에요.



import traceback             #에러 위치를 가져오다

num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]
idx = 0
                             ## unm의 숫자 리스트를 0의 위치부터 찾겠다.
try:                         # 이 안의 코드를 실행해보자.
    while True:
        idx = num_list.index(3,idx) # ValueError: 3 is not in list
        print(f'3 은 {idx} 인덱스에 있습니다.')
        idx += 1

except ValueError as e:     #except “만약 에러가 터지면, 여기서 처리하자”
                            #as e : 에러를 변수 e에 담아서 -> 나중에 메시지로 출력
    print(e)  # 예외에 대한 대략적인 정보 출력
    traceback.print_exc()  # 상세한 예외 정보(개발자에게 필요한 정보)
    print('더이상 3을 찾을 수 없습니다.')
finally:
    print('====끝====')
