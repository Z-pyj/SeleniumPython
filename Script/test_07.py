# 删除序列相同元素并保持顺序,set、list、dict 三个类型是不可哈希的
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题
def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


var = [1, 5, 2, 1, 9, 1, 5, 10]


# 不可哈希（比如 dict 类型）的序列中重复元素
# key 参数指定了一个函数，将序列元素转换成 hashable 类型
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
var1 = list(dedupe2(a, key=lambda d: (d["x"], d["y"])))
print(var1)

var2 = list(dedupe2(a, key=lambda d: d['x']))
print(var2)

# 切片命名，方便阅读
# 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方
var3 = [1, 5, 2, 1, 9, 1, 5, 10]
a = slice(2, 7, 2)
var4 = var3[a]
print(var4)

# 序列中出现次数最多的元素
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

# 获取出现次数最多的3个元素
# 作为输入，Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象
str5 = Counter(words).most_common(3)
print(str5)

# 通过某个关键字排序一个字典列表
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

# 过滤序列元素
# 列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
var5 = [n for n in mylist if n > 0]
print(var5)

# 生成器迭代
var6 = (n for n in mylist if n > 0)
for i in var6:
    print(i)

# 将过滤代码放到一个函数中，然后使用内建的 filter() 函数

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


var7 = list(filter(is_int, values))
print(var7)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

# 你想构造一个字典，它是另外一个字典的子集
# 最简单的方式是使用字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 100}
print(p1)  # {'AAPL': 612.78, 'IBM': 205.55}
