#设计一个闹钟类
class clook:
    id=None
    price=None
    def ring(self):
        import winsound
        winsound.Beep(3000,3000)

#面向类设计对象,构建闹钟对象并让他工作
clock1=clook()
clock1.id="001"
clock1.price=100
print(f"闹钟的编号是：{clock1.id},闹钟的价格是：{clock1.price}")
clock1.ring()

clock2=clook()
clock2.id="002"

clock2.price=100.66
print(f"闹钟的编号是：{clock2.id},闹钟的价格是：{clock2.price}")
clock2.ring()