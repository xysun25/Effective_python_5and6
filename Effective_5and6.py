# -*- coding: utf-8 -*-
# 了解切割序列的办法：把序列切成小块，slice切片操作，对内置的list,str,bytes进行切割
# 例子：somelist[start:end],结束索引所指元素不包括在切割结果中
import os, sys
a=['a','b','c','d','c','d','e','f','g','h']
print ("First four:",a[:4])   # 一个范围，开始索引和结束索引之间的列表元素
print ("Last four:",a[-4:])
print ("Middle two,",a[3:-3])

# 对原列表切割后，可以产生新列表
b=a[4:]
print(b[-2:])
b[1] = 'z'     # 一个索引，一个元素
print (b)

b[3:5] = ['chen','jun','wu']
print (b)
c = a[:]
print (c)

# 在单次切片操作内，不要同时指定start end 和stride
d = ['red','orange','yellow','green','blue','purple']
odds = d[::3]    # 取单数索引元素  3是进步值
evens = d[1::2]  # 取偶数索引元素
print (odds)
print (evens)


