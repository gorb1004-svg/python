# 이렇게 사용하는 함수 2개가 있다.
# 1) from 모듈 import 함수
# -> 사용할 함수를 미리 불러놓고 사용하는 방법
# -> 도시락을 먹을 때 '온갖' 도시락 뚜껑을 열어놓고 먹는 사람
from oper import sum                                             # oper 모듈로부터 sum을 가져온다.
print(f'sum() 함수 실행 : {sum(5,10)}')


# 2) import 모듈
# -> 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법
# -> 도시락을 먹을 때 '먹을' 도시락 뚜껑만 열어놓고 먹는 사람
import oper as op                                                # oper 모듈 전체를 가져오되, 이름을 op라는 별명으로 바꿔서 사용한다.
print(f'minus() 함수실행 : {op.minus(10,5)}')


# 변수도 불러올 수 있다.                                            # oper 모듈에서 변수를 불러올 수 있다.
print(f'filed1 : {op.field1} / filed2 : {op.field2}')             # 왜에 오퍼라는 이름이 op로 사용하겠다. 라고 변경되어 op라는 이름으로 사용하겠다.

