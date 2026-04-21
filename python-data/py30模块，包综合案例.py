#创建my_utils包,在包内创建：str_util.py和file_util.py 2个模块，并提供相应函数
import my_utils.str_utils
from my_utils import file_utils

print(my_utils.str_utils.str_reverse("陈金菊"))
print(my_utils.str_utils.substr("韩淑娴",0,1))


file_utils.append_to_file("D:/text_append.txt","老弟老弟")
file_utils.print_file_info("D:/text_append.txt")









