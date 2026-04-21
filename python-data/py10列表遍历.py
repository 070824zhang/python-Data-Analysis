def list():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """

    my = ["tom","joan","joan"]
    #循环控制变量通过下标索引来控制，默认0
    #每一次循环将下标索引变量加1
    #循环条件：下标索引变量 <  列表的元素数量

    #定义一个变量用来标记列表的下标
    index = 0       #初始下标为0
    while index < len(my):
        element = my[index]
        print(f"列表的元素：{element}")
        index += 1

#list()

def list1():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my1 = [1,2,3,4,5]
    #for   临时变量  in  数据容器：
    for element in my1:
        print(f"列表的元素有：{element}")

list1()
