from sys import stdin, stdout

mod = 10000

line = stdin.readline()
while line:                 # same as while line != '':
    a, op, b = line.split(" ")
    left = int(a)
    right = int(b)
    if op == "+":
        stdout.write(str((left + right) % mod))
        stdout.write('\n')
    elif op == "*":
        stdout.write(str((left * right) % mod))
        stdout.write('\n')
    elif op == "^":
        stdout.write(str(pow(left, right, mod)))
        stdout.write('\n')
    line = stdin.readline()
