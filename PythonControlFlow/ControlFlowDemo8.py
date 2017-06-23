#print和import的更多信息
#print在python3中是一个函数.将字符串或者其他类型转换成字符串输出
#print
#使用逗号输出，可以输出多个表达式
#使用print直接输出1，2，3，不会变成元祖，需要加括号

print(1,2,3)
print((1,2,3))

#import
#import用来导入模块中的函数
#在导入的过程中可以添加别名
import math as foobar
#或者给函数名提供别名
from math import  sqrt as faator


#更多赋值操作
#序列解包
x,y,z=1,2,3
print(x,y,z)
#交换变量
x,y=y,x
print(x,y,z)
#以上过程叫做序列解包(将多个值得序列解开，然后放到变量的序列中)
values=1,2,3
print(values)
x,y,z=values
print(x)

dic={'name':'cy','age':'12'}
key,value=dic.popitem()
print(key)
print(value)
#python3中的新特性
a,b,*c=1,2,3,4,5
print(c)

#链式赋值
#链式赋值是将同一个值给多个变量的捷径，他看起来有些像上节中的并行赋值，不过这里只处理一个值
d=e=4
#也可以是
d=4
e=d
#但是下面不一定等价
d="x"
c="x"

#增量赋值
x=2
x+=1
print(x)

