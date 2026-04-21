class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#str魔术方法
    def __str__(self):
        return f"Student类对象,name: {self.name},age: {self.age}"

 # it魔术方法  小于或者大于
    def __lt__(self, other):
        return self.age < other.age
#le魔术方法
    def __le__(self, other):
        return self.age <= other.age
#eq魔术方法
    def __eq__(self, other):
        return self.age == other.age
stu1 = Student("周杰伦",30)
stu2 = Student("林俊杰",36)
print(stu1==stu2)