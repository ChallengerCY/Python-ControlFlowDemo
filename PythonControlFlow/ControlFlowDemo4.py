#循环结构for循环
#尽量使用for循环，不用while，for循环同样可以使用else，并且嵌套分支结构
word=['this','is','an']
for word in word:
    print(word)

num=[1,2,3,4,5,6]
for num in num:
    print(num)

#range函数,工作方式类似于分片，包含下限，但是不包含上限,range函数中也有步长
for num in range(1,10):
    print(num)

#循环遍历字典元素
d={"x":1,"y":2}
for i in d:
    print(i,d[i])
#for循环可以在循环过程中序列解包
for key,value in d.items():
    print(key,value)