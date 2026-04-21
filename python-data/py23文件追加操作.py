# #打开文件，不存在的文件
# f = open("D:/tes.txt","a",encoding="utf-8")
# #write写入
# f.write("你好，小陈")
# #flush刷新
# f.flush()
# #close关闭
# f.close()
#打开一个存在的文件
f = open("D:/tes.txt","a",encoding="utf-8")
#write写入，flush刷新
f.write("\n哈哈哈小张")
#close关闭
f.close()