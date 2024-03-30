import math
import sys

result = "not applicable"
i = input()
a, b, c, d, k = map(lambda x: float(x), i.split(" "))

log_b_a = math.log(a, b)

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def parseFloat(f):
    if float.is_integer(f):
        return int(f)
    else:
        r = round_half_up(f, 1)
        return int(r) if float.is_integer(r) else r

def n(exponent):
    if exponent == 0:
        return ""
    elif exponent == 1:
        return "n"
    else:
        return f'n^{parseFloat(exponent)}'

def log(base):
    if base == 0:
        return ""
    elif base == 1:
        return "log n"
    else:
        return f'log^{parseFloat(base)} n'

if log_b_a > d:
    # case 1
    result = n(log_b_a)
if log_b_a == d:
    # case 2
    if k >=0:
        result = f'{n(log_b_a)} {log(k+1)}'
    if k == -1:
        result = f'{n(log_b_a)} log log n'
    if k < -1:
        result = f'{n(log_b_a)}'
if log_b_a < d:
    # case 3
    result = f'{n(d)} {log(k)}'

print(result)
