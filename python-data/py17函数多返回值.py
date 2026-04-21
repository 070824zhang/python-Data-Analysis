#使用多个变量，接收多个返回值
def test_return():
    return 1,"hello",True

x,y,z = test_return()
print(x,y,z)

