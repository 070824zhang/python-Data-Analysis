#定义集合
shiren = {"libai","dufu","sushi"}
shirenmy = set()
print(f"shiren的内容是{shiren},类型是：{type(shiren)}")
print(f"shirenmy的内容是{shirenmy},类型是：{type(shirenmy)}")

#添加新元素
shiren.add("lishangyin")
shiren.add("xinqiji")
print(f"shiren添加元素后结果是：{shiren}")

#移除元素
shiren = {"libai","dufu","sushi"}
shiren.remove("libai")
print(f"shiren移除libai后结构是:{shiren}")

#随机取出一个数字
shiren = {"libai","dufu","sushi"}
element = shiren.pop()
print(f"集合被取出元素是：{element},取出元素后：{shiren}")

#清空集合
shiren.clear()
print(f"集合被清空啦，结果是{shiren}")

#取2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set.difference(set2)
print(f"取出差集后的结果是：{set3}")

#消除差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")

#两个集合合并为一个
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"2集合合并结果：{set3}")
print(f"合并后集合1：{set1}")
print(f"合并后集合2：{set2}")

#统计集合元素数量len（）
set1 = {1,2,3,4,5,1,2,3,4,5}
num = len(set1)
print(f"集合内元素数量有：{num}个")

#集合遍历
#不支持下标索引，不能用while循环，能用for
set1 = {1,2,3,4,5,1,2,3,4,5}
for element in set1:
    print(f"集合的元素有：{element}")

