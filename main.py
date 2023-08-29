n = int(input())

def p(k):
    a = k.split()
    return int(a[0]), int(a[1])

ab = sorted(map(p, (input() for _ in range(n))))

lb = ab[0][1]
for i in range(1, n):
    j = ab[i][1]
    if j < lb:
        print("Happy Alex")
        raise SystemExit()
    lb = j

print("Poor Alex")
