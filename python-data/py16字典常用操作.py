my = {"周杰伦":99,"林俊杰":88,"张学友":77}
#新增元素
my["张信哲"] = 66
print(f"字典新增元素后，结果：{my}")
#元素更新
my["周杰伦"] = 33
print(f"字典更新后，结果：{my}")
#删除元素
score = my.pop("周杰伦")
print(f"字典被移除一个元素后，结果：{my}，周杰伦的考试分数是：{score}")
#清空元素
my.clear()
print(f"字典被清空了，结果：{my}")

#获取字典中全部的key
my = {"周杰伦":99,"林俊杰":88,"张学友":77}
keys = my.keys()
print(f"字典的全部key是：{keys}")

#遍历字典
#方式一： 通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my[key]}")

#方式二：  直接对字典进行for循环，每一次循环都是直接得到key
for key in my:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my[key]}")

#统计字典的元素数量，len()
num = len(my)
print(f"字典中的元素数量有：{num}个")


