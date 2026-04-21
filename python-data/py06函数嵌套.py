#定义函数func_b
def func_b():
    print("---2---")
#定义函数func_a,并在内部调用func_b
def func_a():
    print("---3---")


    #嵌套调用func_b
    func_b()
    
    print("---4---")
#调用函数func_a
func_a()