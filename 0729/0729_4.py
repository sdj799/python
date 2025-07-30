class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)
    
p = Person.from_birth_year("홍길동", 1980)
print(p.name, p.age)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def mul(a,b):
        return a * b
    
print(MathUtils.add(1,2))
print(MathUtils.mul(1,2))