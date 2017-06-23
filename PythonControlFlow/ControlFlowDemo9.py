#pass del exec
#pass可以在代码中做占位符使用
#如果代码中存在空代码块，是非法的，需要用pass跳过，pass与注释联合的代替方案是插入字符串,被插入的字符串扮演文档字符串
name='c'
if name=='a':
    print(name)
elif name=='b':
    print(name)
elif name=='c':
    #sad
    pass

#del
#如果一个字典被绑定到俩个不同的变量上，并且给这俩个变量赋予None，则原本的字典会被垃圾回收
#del不仅会移除一个对象的引用，也会移除那个名字本身,如果对象还被关联到其他变量上，该关联不会受到影响，Python中不需要过多的考虑删除值，因为会自动回收
x=1
y=x
del x
print(y )

#exec和eval
#exec 用于执行一个字符串中的python代码
exec('print("hello world")')
#防止从外界得到不需要的代码，可以设立字典来隔离
from math import sqrt
scope={}
exec('sqrt=1',scope)
print(sqrt(4))
print(scope["sqrt"])
#eval(用于"求值")，类似于exec，执行字符串中的表达式，并返回结果值
print(eval(input()))
#在python中没有任何执行不可信任代码的安全方式，一个方法是使用python的实现，比如jyhon，还有一些本地机制，比如java的sandbox功能