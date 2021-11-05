import numpy


def drop_first_last(grades):
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