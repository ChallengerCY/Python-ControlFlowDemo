#循环结构while语句
#当while 后面的条件为真时，循环会一直执行，也就是死循环，while后面可以加else
x=1
while x<=100:
    print(x)
    x=x+1
else:
    print("超出100")

#循环与分支嵌套
a=1
while a<10:
    if a<=5:
        print(a)
    else:
        print("hello")
    a=a+1
else:
    print("test")

#while True/Break
#该方法实现了一个永远不会自己停止的循环，但在循环内部的if语句中加入条件，满足时调用break，就可以在循环内部任何地方终止循环。
while True:
    word=input()
    if not word:
        break
    print(word)