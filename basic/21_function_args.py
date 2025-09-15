# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능


#def 정의한다.

#def 함수를 쓸거야.
#plus 함수명
#num 매개변수이름(아무 값도 없으면 0을 넣을거야.)
# result 일반 변수.

def plus(num=0):                                # num이라는 매개변수를 쓸 건데, num 값이 안들어오면, 0을 쓸거야.
    result = num +5
    return result

print(plus(5))          ### 10
print(plus())           ### plus() missing 1 required positional argument: 'num'
                        # ->> 사용자가 실수를 할 수 있기에, 기본값을 0으로 넣어준다.
#-> 회원가입을할 때 아무것도 안넣어도 생성이되는 것들. 기본으로 알아서 채워 넣어줌.

# args 인자값들
# 인자값의 종류를 튜플(수정이 불가능한 List 형태)로만 받겠다.
def tuple_args(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# 쇼핑할때 장바구니에 물건을 담을 때, 몇개를 넣을지 모르겠어. 모르는 개수만큼 다 더해줄게
# * 물겁값을 다 더할때


# 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))

# ** 매개변수를 사전형태로 받겠다.
def dic_args(**dic):
    print(dic)

# 위 함수를 실행하면 입력된 값들의 합산이 반환되도록 하세요.
result = dic_args(kim=50, lee=100, park=70, na=90)

# ** 마우스와 마우스의 정보를 불러오고 싶을 때

#------------------
    # def dic_args(**dic)
# 1) dic 에서 값만 빼온다.

# 2) 이 값들을 하나씩 더해 누적시킨다
# 3) 누적시킨 값을 밖으로 return 한다.
# print(dic)
#------------------



# 문제를 단순화 시키고
# 살려주세요, 어디신가요. 상황이 어떤가요.
# 내가 뭘하고싶은지 상세하게 기록해야 해요.
# 내가 뭘하고싶은지 어떤순서로 뭘하고싶은지 적어야함.


