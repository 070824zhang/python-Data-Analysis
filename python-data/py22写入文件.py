import time
#打开文件，不存在的文件
# f = open("D:/test.txt","w",encoding="utf-8")
# #f.write写入
# f.write("hello world")   #内容写入到内存中
# #  flush刷新
# f.flush()                #将内存中积攒的内容，写入到硬盘的文件中
# #close关闭
# f.close()                #close方法，内置了flush的功能
#打开一个存在的文件
f = open("D:/test.txt","w",encoding="utf-8")
#write写入，fluse刷新
f.write("我喜欢你，小韩")
#close关闭
f.close()