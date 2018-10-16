#!/usr/bin/env python3
from collections import namedtuple

Timestamp = namedtuple('Timestamp', ['h', 'm', 's'])
Timestamp.__str__ = lambda self: "{h:02}:{m:02}:{s:02}".format(
    h=self.h, m=self.m, s=self.s
)

def get_timestamp(s):
    slices = (
        (0, 2), (3, 5), (6, 9),
    )
    return Timestamp(*(int(s[l:r]) for l, r in slices))

SECS_IN_MINUTE = 60
SECS_IN_HOUR   = SECS_IN_MINUTE * 60
SECS_IN_DAY    = SECS_IN_HOUR * 24

def get_seconds(t):
    ret =  t.h * SECS_IN_HOUR
    ret += t.m * SECS_IN_MINUTE
    ret += t.s
    return ret
Timestamp.__int__ = get_seconds

def get_timestamp_from_seconds(secs):
    h = secs // SECS_IN_HOUR
    h %= 24
    secs %= SECS_IN_HOUR
    m = secs // SECS_IN_MINUTE
    secs %= SECS_IN_MINUTE
    s = secs
    return Timestamp(h, m, s)

A, B, C = [int(get_timestamp(input())) for _ in range(3)]

tm2 = 2*B + (C-A) % SECS_IN_DAY
tm = tm2 // 2 + tm2 % 2
tm = get_timestamp_from_seconds(tm)
print(tm)
