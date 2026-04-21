#定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")


#定义单个元素的类型
t4 = ("hello",)
print(f"t4类型是：{type(t4)},内容是：{t4}")


#元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5类型是：{type(t5)},内容是：{t5}")

#下标索引取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

#元组的操作 :index查找方法
t6 = ("tom","jesan","jare")
index = t6.index("tom")
print(f"在元组t6中查找黑马程序员的下标是:{index}")

#count  统计的方法
t7 = ("tom","jesan","jare","tom","tom")
num = t7.count("tom")
print(f"在元组t7中统计tom的数量有：{num}个")

#len函数统计元组元素数量
t8 = ("tom","jesan","jare","tom","tom")
num = len(t8)
print(f"t8元组中的元素有：{num}个")

#元组的遍历
#while循环
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1

#for循环
for element in t8:
    print(f"2元组的元素有：{element}")

#定义一个元组
t9 = ("tom","jesan","jare",["tom","jare"])
print(f"t9的内容是：{t9}")
t9[3][0] = "汤姆"
t9[3][1] = "杰瑞"
print(f"t9的内容是：{t9}")



