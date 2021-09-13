# coding:utf-8

with open(0) as f:
    lines = f.read().splitlines()

N = int(lines[0])
i = 0

while N != 1:
    print('{} 回目: {}'.format(i, N))
    if N % 2 == 0:
        N = int(N/2)
    else:
        N = int(3*N+1)
    i += 1

print('{} 回目: {}'.format(i, N))
