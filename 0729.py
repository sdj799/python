# 클래스
# 객체를 생성하기 위한 설계도

# 클래스 - 붕어빵 틀
# 객체는 - 실제 붕어빵
# 속성(변수) - 붕어빵의 특징(크기, 맛, 색깔)
# 매서드(함수) - 붕어빵이 할 수 있는 행동(먹히기, 식히기)

class 클래명:
    # 클래스 내용
    pass

class Person:
    # 생성자
    # 객체가 생성될때 자동으로 호출되는 매서드
    # 초기 상태를 설정하는 역할

    # self 키워드
    # 현재 인스턴스 자신을 가리키는 참조
    # 모든 인스턴스 매서드의 첫번째 매개변수
    # 인스턴스 변수와 메서드에 접근할때 사용
    def __init__(self, name, age):
        self.__name = name # 인스턴스 변수
        self.__age = age

# 소멸자
    def __del__(self):
        # 객체가 사라질때 자동으로 호출되는 매서드
        print(f"{self.name} 삭제되었습니다.")
    
    def introduce(self): # 인스턴스 메서드
        print(f"안녕하세요! 제 이름은 {self.__name} 이고, {self.__age}살 입니다.")

    @property
    def name(self):
        return self.__name
    
    # def getName(self):
    #     return self.name
    @name.setter
    def name(self, name):
    #def setName(self, name):
        self.__name = name

    @property
    def age(self):
    # def getAge(self):
        return self.__age
    
    @age.setter
    def age(self, age):
    # def setAge(self, age):
        self.__age = age
    
    
# 객체 생성 (인스턴스화)
person1 = Person("김철수", 25)
person2 = Person("이영희", 20)

person1.introduce()
person2.introduce()

# person1.setName("홍길동")
# person1.setAge(30)
# print(person1.getName())
# print(person1.getAge())
person1.name ="홍길동"
person1.age = 30
print(person1.name)
print(person1.age)

class Caculator:
    PI = 3.14

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        if(self.num2 != 0):
            return self.num1 / self.num2
        return 0
    
c = Caculator(4, 2)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
print(c.PI)

c2 = Caculator(54, 6)
print(c2.add())
print(c2.sub())
print(c2.mul())
print(c2.div())
print(c2.PI)

class Employee:
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름: {self.name}"

emp1 = Employee("김철수")
emp2 = Employee("이영희")

print(emp1)
print(emp2)

class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(f"위치: {self.location}")
    
    def change_category(self, product):
        self.product = product

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        self.customer += 1
    
    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}")


sup = Supermarket("마포구 염리동", "마켓온", "콜라", 11)
sup.print_location()
sup.change_category("음료")
sup.show_list()
sup.enter_customer()
sup.show_info()