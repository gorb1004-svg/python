dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','John']
}

# dic.key(): 특정한 사전의 키들만 가져와 dict_keys 라는 객체를 반환한다.
print(dic.keys())

for item in dic.keys():
    print(item)
                                                  # 8번줄의 print 한 dic.keys의 값들을
                                                  # for문을 사용해서 in dic.keys() 이 for item으로 순서대로 출력 함.

#dict_keys -> list로 변환                          # 반대로 딕키즈를 리스트로 변환
keys = list(dic.keys())
print(keys)

# dic.values(): 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())


# list 로 변경해서 values 라는 변수를 담아보자
values = list(dic.values())
print(values)

# dic.items(): 사전의 키: 값을 한 쌍으로 가져와 dict_item 로 변환한다.
# 각키와 값은() 모양으로 보아 tuple 이다.
print(dic.items())
#list 로 변환해 보면 list 안에 각 키와 값이 튜플로 저장되어 있음을 알 수 있다.
li = list(dic.items())
print(li)

# 값을 가져오기(택1)
print(dic.get('name'))
print(dic['phone'])

#dic 안에 있는 모든 키와 값을 키:값 형태로 출력해보자
# 1. 키를 뽑아낸 다음, 키를 가지고 값을 뽑아내는 방법
   # 키가 있어야, 다른것도 뽑을 수 있다.
for key in dic.keys():
    print(f'{key}:{dic[key]}')

# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for item in dic.items():
    print(f'{item[0]}={item[1]}')

