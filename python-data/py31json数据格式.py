import json
#准备列表，列表内每一个元素都是字典，将其转换为json
data = [{"name":"张大山","age":11},{"name":"周杰伦","age":30},{"name":"林俊杰","age":40}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
#准备字典，将字典转换为json
d = {"name":"周杰伦","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str)
print(type(json_str))
#将json字符串准换为python数据类型[{}{}{}]
s = '[{"name": "张大山", "age": 11}, {"name": "周杰伦", "age": 30}, {"name": "林俊杰", "age": 40}]'
l = json.loads(s)
print(type(l))
print(l)
#将json字符串转换为python数据类型{}{}
s = '{"name":"周杰伦","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)
