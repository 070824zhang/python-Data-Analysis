#定义类
class Stu:
    name=None

    def hi(self):
        print(f"大家好呀，我是{self.name}，请多多关照")


    def hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

stu=Stu()
stu.name="周杰伦"
stu.hi2("哎呦不错哦")

stu2=Stu()
stu2.name="林俊杰"
stu2.hi2("你干嘛")
