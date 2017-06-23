#分支结构if

#if else elif的使用 else 只能作为if的子句 如果有多个条件需要使用elif
#要点:各分支尽量不要重复，并且尽量包含全部可能性
name =input("what you name:")
if name.endswith('CY'):
    print("hello "+name)
elif name.endswith('cc'):
    print('hi '+name)
else:
    print("sorry")

#断言
#if有个近亲 assert
#如果确保程序中的某个条件一定为真才能让程序正常工作,可以在程序中放入assert检查点，在条件后面还可以加上检查点，用来解释断言
age=-1
assert 0<age<100,'The age must be realistic'



