#控制流功能
#重复执行3段同样的程序
#方式一 顺序结构
i=0
print(i)
i=i+1
print(i)
i=0
print(i)
i=i+1
print(i)
i=0
print(i)
i=i+1
print(i)

#方式二 循环结构
for k in range(0,3):
    i = 0
    print(i)
    i = i + 1
    print(i)

a=7
while a:
    print("hello")
    a=a-1

#方式三 分支结构
xiaoming="eat1"
if xiaoming=="eat":
    print(True)
else:
    print(False)