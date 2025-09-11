# 문자열은 "나"" 모두 사용 가능(싱글쿼터, 더블쿼터)
name='kim ji hoon'
content = "my content"

# 여러줄의 문자열을 변수에 담을 때
multi = '''this is multi line string
this is second line'''


print('name:'+name)
print('content:'+content)
print('multi:'+multi)

# 문자열에 다른 타입의 데이터를 함께 출력할 경우...
age = 33

print('내이름은 {0} 이고, 나이는 {1} 입니다.'.format(age,age))
print('내이름은'+name+'이고 나이는 '+str(age)+'입니다.')
#예전에 format을 사용함.
#str를 사용해서 문자가 아닌 녀석을 문자로 변환해서 썼음.

print(f'내이름은 {name}이고, 나이는 {age}입니다.')
####요즘은 f-string을 사용한다고 함.


# 여러줄 -> 한줄 처리, 한줄 -> 여러줄처럼 줄바꿈
print('이것은 한줄이지만\n 여러줄처럼 보이게 할겁니다.')
print('이것은 두줄이지만 \
한줄처럼 보이게 할겁니다.')
# \n은 줄바꿈을 처리함.(뉴라인이라고 부름)




