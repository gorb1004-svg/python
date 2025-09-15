dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','John']
}

# dic.key(): 특정한 사전의 키들만 가져와 dict_keys 라는 객체를 반환한다.
print(dic.keys())
                                                    # 8번줄의 print 한 dic.keys의 값들을 -> dict_keys(['name', 'phone', 'friends'])
for item in dic.keys():                             # for문을 사용함. 사용하면, 순차적으로 이름/폰/친구가 나래비 됌
    print(item)                                     # 딕.키의 내용이 아이템으로 순차적으로 들어 감.



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


members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

# 90이상인 사람의 이름만 출력
for name in members.keys():
    if members.get(name) >= 90 :
        print(name)

        # * members.keys를 적는 이유
        # 1) members는 {딕셔너리}를 담고 있는 변수의 이름
        # 2) .keys 메서드(기능)을 불러올 때 사용함. 키/밸류/아이템이 있음
        # * name를 적는 이유: 변수의 이름은 자유롭게 작성해도 됌

        # 숫자 90 이상인 사람의 이름만 출력하라는 조건임
        # 이상인 사람 이람들을 출력해야되서 반복문인 For문을 사용함. 조건이 만약 멤버 이상
        # for 문 : 90이상인 사람이름 조건이 있음.
        # 멤버스.키를 받아야할 네임
        # 만약 90점 사람의 이름이라면



# update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수
dic.update({'name':'홍길동','age':30,'married':'false'})
print(dic)

# dic.clear() : 사전안의 내용을 모두 지운다.
dic.clear()
print(dic)

