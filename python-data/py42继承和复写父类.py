class Phone:
    id="2021"
    age=1
    def my_phone(self):
        print("欢迎使用4g")
        print("欢迎使用指纹解锁")

#继承父类   单继承
class Phone2024(Phone):
    id="2024"
    age=2
    def my_phone(self):
        print("欢迎使用5g")
        # 复写父类   方式一
        # print(f"父类的年龄：{Phone.age}")
        #Phone.my_phone(self)  #复写父类
        # 复写  方式二
        print(super().id)
        super().my_phone()
        print("欢迎使用face_id")

phone=Phone2024()
print(phone.id)
phone.my_phone()





