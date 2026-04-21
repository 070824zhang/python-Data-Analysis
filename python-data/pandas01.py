import pandas as pd
#1.模拟一个简单的成绩单
data = {'姓名':['小王','小李','小张'],'得分':[85,92,58]}
df = pd.DataFrame(data)
#这里的df['得分']其实就是一个Series
scores = df['得分']
print("平均分是：",scores.mean())
print("及格名单：\n",df[scores >= 90])  #筛选出及格的人