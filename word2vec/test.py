#-*- coding: utf-8 -*-
a = u'China'
b = 'China'
c = u'中国'
d = '中国'
# 1
print '%s %s' % (a, b)
# 2
print '%s' % c
# 3
print '%s' % d
# 4
print '%s %s' % (c, d)