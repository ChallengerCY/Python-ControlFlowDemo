#break语句
#break常用于循环结构，能将该循环强制停止

#在while中使用break
a=1
while a:
    print(a)
    a=a+1
    if a==10:
        break

#在for循环中使用break
for i in range(1,8):
    print(i)
    if(i==5):
        break

#在嵌套语句中的循环使用
a=10
while a<=12:
    a=a+1
    for i in range(1,7):
        print(i)
        if i==5:
            break
    if a==11:
        break