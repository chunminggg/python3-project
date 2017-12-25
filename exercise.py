#字符串内容
import string
chars = string.ascii_letters + string.digits
#返回abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
import random
def getrandom():  #定义一个函数，将一个含有4个随机元素的列表内的元素合并在一起组成一个字符串
    return "".join(random.sample(chars, 4)) 

def concatenate(m): #定义一个函数，将m个4元素字符串用“-”连接起来组成一个激活码
    return "-".join([getrandom() for i in range(m)])

def generate(n): #定义一个函数，返回n个激活码组成的列表
    return [concatenate(4) for i in range(n)]     
if __name__ == '__main__':
    for item in generate(10): #把列表里的10个激活码打印出来
       