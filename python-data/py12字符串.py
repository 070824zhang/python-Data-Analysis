my = "libai666 and dufunb"
#通过下标索引取值
t1 = my[1]
t2 = my[-6]
print(f"从字符串{my}取下标为1的元素值是{t1},以及取下标为-6的元素值是：{t2}")
#my[2] = "a"


#index方法
t3 = my.index("libai666")
print(f"在字符串{my}中查找libai666，其起始下标是:{t3}")

#replace方法
new_my = my.replace("libai666", "hello")
print(f"将字符串{my},进行替换后得到：{new_my}")

#solit语法
my = "hello python libai dufu"
t1 = my.split(" ")
print(f"将字符串{my}进行split切分后得到;{t1},类型是：{type(t1)}")

#strip方法
my = "   libai and dufu    "
t2 = my.split()    #不传入参数，去除首尾空格
print(f"字符串{my}被strip后结果是：{t2}")

my = "12libai and dufu12"
t3 = my.split("12")
print(f"字符串{my}被strip('12')后结果是：{t3}")


