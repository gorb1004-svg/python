# 사전은 키:값 형태로 되어있다.
# 비슷한 자료구조로는 자바스크립트에 오브젝트, 자바의 맵이 있다.

#[] 리스트
#() 튜플
#{} 딕셔너리 , 얘는 리스트와 같다고 했습니다. 문자가 들어갈 뿐이지.
#[:] 슬라이싱

dic = {
    'name':'kime,ji-hoon',
    'phone':'010-1234-1234',
    'age':55
}

dic2 = {
    'name':'hong,gil-dong',
    'phone':'010-2233-5454',
    'friends':['Alice','John','Smith']
}

print(dic)
print(dic2)


# 사전에 데이터 넣기 1
a = {'first':'a'}          # 딕셔널리{키:밸류}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자(사용법은 List 와 비슷하다)
print(dic2['name'])
print(dic2['friends'])
print(dic2.get('phone'))

# 특정 키가 없는 경우 NOne 이 아닌 대체 내용으로 변환할 수 있음.
print(dic2.get('nick','해당 내용이 없음'))
