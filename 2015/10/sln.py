#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# part 1
s = '1321131112'
for i in range(40):
    n = ''
    last, cnt = s[0], 1
    for c in s[1:]:
        if last == c:
            cnt += 1
        else:
            n += str(cnt) + last
            last, cnt = c, 1
    s = n + str(cnt) + last
print(len(s))


# part 2
s = '1321131112'
for i in range(50):
    n = ''
    last, cnt = s[0], 1
    for c in s[1:]:
        if last == c:
            cnt += 1
        else:
            n += str(cnt) + last
            last, cnt = c, 1
    s = n + str(cnt) + last
print(len(s))
