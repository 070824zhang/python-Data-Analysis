my = ["tom","joan","jire"]
#查找某元素在列表内的下标索引


index = my.index("tom")
print(f"tom在列表中的下标索引值是：{index}")
#如果被查找的元素不存在，会报错


#index = my.index("hello")
#print(f"tom在列表中的下标索引值是：{index}")


#修改特定下标索引的值
my[0] = "okkk"
print(f"列表被修改元素值后，结果是：{my}")

#在指定下标位置插入新元素
my.insert(1,"lele")
print(f"列表插入元素后，结果是：{my}")

#在列表的尾部追加'''单个'''新元素
my.append("zizizi")
print(f"列表在追加了元素后，结果是{my}")

#在列表的尾部追加一批元素
my2 = [1,2,3]
my.extend(my2)
print(f"列表在追加了一个新的列表后，结果是{my}")

#删除指定下标索引的元素（两种方式）
my = ["tom","joan","jire"]
#方式1：del 列表[下标]
del my[2]
print(f"列表删除元素后结果是：{my}")
#方式二： 列表.pop(下标)
my = ["tom","joan","jire"]
element = my.pop(2)
print(f"通过pop方法取出元素后，列表内容：{my},取出的元素是{element}")

#删除某元素在列表中的第一个匹配项
my = ["tom","joan","jire","libai","dufu","libai"]
my.remove("libai")
print(f"通过remove方法移除元素后，列表的结果是：{my}")


#清空列表
my.clear()
print(f"列表被清空了，结果是{my}")


#统计某元素出现的次数
my = ["tom","joan","jire","libai","dufu","libai"]
count = my.count("libai")
print(f"列表中libai的数量是{count}个")


#统计列表中全部元素的数量
my = ["tom","joan","jire","libai","dufu","libai"]
count = len(my)
print(f"列表中的元素数量总共有{count}")