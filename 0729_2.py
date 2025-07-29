class Info:
    def __init__(self, breed):
        self._breed = breed

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f"동물 소리를 냅니다."

    def move(self):
        return f"동물이 움직입니다."

class Dog(Animal, Info):
    def __init__(self, name, age, breed):
        # 슈퍼 클래스(부모 클래스) 생성자 호출
        Animal.__init__(self, name, age)
        Info.__init__(self, breed)
        # self.breed = breed

    # 매서드 오버라이딩
    def speak(self):
        # return super().speak()
        return f"{self._name}: 멍멍!"
    
    # 서브 클래스 고유 매서드
    def tail(self):
        return f"{self._name}이(가) 꼬리를 흔듭니다!"
print("=========== 상속 ==========") 
dog = Dog("멍멍이", 3, "진돗개")
print(dog.move()) # 부모 클래스
print(dog.speak()) # 오버라이딩
print(dog.tail()) # 자식 클래스

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period = 12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 연장되었습니다. 현재 보증 기간: {self.warranty_period}개월")

    def display_info(self):
        super().display_info()
        print(f"보증기간: {self.warranty_period}개월")

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    def is_expired(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name}는 유통기한이 지났습니다")
        else:
            print(f"{self.name}는 유통기한이 지나지 않았습니다")


    def display_info(self):
        super().display_info()
        print(f"유통기한: {self.expiration_date}")
    
tv = Electronic("스마트 TV", 1500000, 5, 24)
tv.extend_warranty(12)
tv.display_info()

apple = Food("사과", 3000, 50, "2025-07-30")
apple.is_expired("2025-07-29")
apple.display_info()