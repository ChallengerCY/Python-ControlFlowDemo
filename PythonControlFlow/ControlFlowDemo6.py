#迭代工具
#并行迭代
#zip函数可以用来进行并行迭代
#zip函数将两个序列压缩到一起，返回一个元祖，可以处理不等长的序列，当最短序列用完的时候就会停止
name=['Challenger','CY']
age=[11,12]
for name,age in zip(name,age):
    print(name,age)

#索引迭代
#enumerate函数可以在提供索引的地方迭代索引-值对
strings="abcdecfg"
for index,string in enumerate(strings):
    if 'c' in string:
        print(strings[index],index)

#翻转和排序迭代
#reversed和sorted函数，它们与列表的reverse和sort类似，但不是原地修改对象，而是返回翻转或排序后的版本,sorted返回一个列表，reversed函数返回一个可迭代对象
print(sorted([4,5,8,7,25,3]))

print(sorted("hello world!"))

print(list(reversed("hello world!")))

print(''.join(reversed("hello world!")))

#列表推导式
#是利用其他列表创建新的列表
print(list(x*x for x in range(10)))
#打印出可以被三整除的数
print(list(x*x for x in range(10) if x%3==0))
#也可以加入更多的for语句部分
print(list((x,y) for x in range(3) for y in range(3)))

#最优方案查找男女名字匹配
girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
letterGirls={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print(list(b+'+'+g for b in boys for g in letterGirls[b[0]]))
