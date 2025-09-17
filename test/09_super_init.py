# 생성자 전달 순서 설명

class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() #생략된 부모 생성자
        print('자식 생성자 실행!')

ch=Child()

# 부모가 초기화가 필요 하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember: # 부모
    name =''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    salary = 0
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

t = Teacher('김철수',33,500)
print(t.name)
print(t.age)
print(t.salary)

print(f'이름 {t.name}, 나이 {t.age}, 연봉 {t.salary}')

