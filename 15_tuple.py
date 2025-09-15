# 리스트와 다른점이 수정삭제 안되고, 대괄호대신 소괄호를 사용한다.

tu1 = (1,2,3) # tulpe은 [] 가 아닌 () 로 선언
tu2 = ('a','b','c')
tu3 = (1,2,('a','b'))

print(tu1[1])
# slicing
print(tu2[1:])     #1번부터 보여지고
# 더하기
print(tu1+tu2)
# 곱하기
print(tu1*3)


#리스트인게 가능한게 있고, 튜플인게 가능한게 있다고 했죠?
#리스트는 수정삭제가 가능, 튜플은 보이게만 가능
#튜플에서 리스트로 변경도 가능함.(전환)

# tuple <-- -->list 간의 전환
tu2list = list(tu2)
print(f'{tu2}->{tu2list}')
#튜2리스트와 리스트이다.
#f스트링으로 튜2출력해. 리스트로



list2tu = tuple(tu2list)
print(f'{tu2list}->{list2tu}')

