class Student:
    name = None
    age = None
    gender = None
    country = None

#创建一个对象
stu_1 = Student()
#将对象属性进行赋值
stu_1.name = "小张"
stu_1.age = 20
stu_1.gender = "male"
stu_1.country = "China"
#获取对象中的信息
print(stu_1.name)
print(stu_1.age)
print(stu_1.gender)
print(stu_1.country)