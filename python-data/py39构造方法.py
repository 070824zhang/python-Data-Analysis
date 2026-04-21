class Student:
    def __init__(self, name, age, site):
        self.name = name
        self.age = age
        self.site = site


for i in range(10):
    print(f"当前录入第{i+1}位学生信息，总共需要录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    site = input("请输入学生地址：")
    stu = Student(name, age, site)
    print(f"学生{i+1}的信息录入完成，信息为：【学生姓名：{stu.name},年龄：{stu.age},地址：{stu.site}】")