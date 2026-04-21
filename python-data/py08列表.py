"""
语法：[元素，元素，元素.....]
"""

#定义一个列表list

my = ["lisa","python","python"]
print(my)
print(type(my))


mylisa = ["lisa",666,True]
print(mylisa)
print(type(mylisa))

#定义一个嵌套的列表
my = [[1,2,3],[4,5,6]]
print(my)
print(type(my))

#通过下标索引取出对应位置的数据
my = ["tom","jasen","yohan"]
#列表[下标索引]，从前向后从0开始，每次加一，从后向前从-1开始，每次-1
print(my[0])
print(my[1])
print(my[2])
#通过下标索引取出数据，一定不要超出范围

#倒序取出
print(my[-1])
print(my[-2])
print(my[-3])

#取出嵌套列表的元素
my = [[1,2,3],[4,5,6]]
a = my[1][1]
print(a)
