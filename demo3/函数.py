def printInfo():
    print("-"*30)
    print("hello world")
    print("*"*30)

printInfo()

#返回多个值的函数
def divid(a,b):
    shang = a/b
    yushu = a%b
    return shang,yushu #多个返回值用逗号分隔

sh,yu=divid(5,2)
print("商：%d, 余数：%d"%(sh,yu)) #需要使用多个值来保存返回内容
