#Continue语句
#Continue语句的功能是强制停止循环中的这一次执行，直接跳到下一次执行
#在while中使用continue
a=1
while a<7:
    a=a+1
    if a==3:
        continue
    print(a)

#在for循环中使用continue
for i in range(1,7):
    if i==3:
        continue
    print(i)

#在双层循环中使用continue
a=1
while a<7:
    a=a+1
    if a==4:
        continue
    for i in range(7,10):
        if i==9:
            continue
        print(i)