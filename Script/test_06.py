import numpy
from typing import *
import heapq
from collections import deque
from collections import defaultdict


def drop_first_last(grades: List) -> float:
    first, *middle, last = grades
    return numpy.average(middle)


def test01(money):
    *arg, last = money
    print("前几个月的平均收入为:%s" % numpy.average(arg))
    print("最后一个月的收入为:%s" % last)


grade = drop_first_last([22, 44, 55, 66, 77, 44, 46])

test01([333, 66, 22, 53, 8786, 3454, 454, 34, 34535, 445])

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def foo(x, y):
    print("foo", x, y)


def bar(x):
    print("bar", x)


for tag, *args in records:
    if tag == "foo":
        foo(*args)
    if tag == "bar":
        bar(*args)

# 星号解压语句，在字符串操作的时候也很有用
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(homedir)
print(sh)

# 解压后丢弃，使用ign或者_表示
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print("name:%s , year:%s" % (name, year))

# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
# 且这个队列已满的时候，最老的元素会自动被移除掉。
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元素的时间复杂度为 O(N)

# 从一个集合中获得最大或者最小的 N 个元素列表
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
hq_max = heapq.nlargest(3, nums)
hq_min = heapq.nsmallest(3, nums)
print(hq_max, hq_min)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 可以接受key，用于复杂的数据
hq_list = heapq.nsmallest(3, portfolio, key=lambda k: k["price"])
print(hq_list)

"""
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。如果你仅仅想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和max() 函数会更快些。类似的，如果 N 
的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点（sorted(items)[:N] 或者是 sorted(items)[-N:]）
"""

# 字典中的键映射多个值

pairs = [("a", 1), ("b", 2), ("a", 2), ("a", 3)]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

# 字典保持插入时的顺序
ordered = {'name': 'IBM', 'shares': 100, 'price': 91.1}
print(ordered)

# 数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
