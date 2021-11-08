# 使用多个界定符分割字符串
# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
var8 = re.split(r"[;,\s]\s*", line)
print(var8)

# 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# 通过指定的文本模式去检查字符串的开头或者结尾
filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:')
# 检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith() 方法
import os

filenames = os.listdir('.')
var1 = [name for name in filenames if name.endswith(('.c', '.h'))]
print(var1)


