def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if d[n] > 0:
        return d[n]
    d[n] = (fibo(n-1) + fibo(n-2))
    return d[n]

n = int(input())
d = [0 for i in range(n+1)]
n = fibo(n)

print(n)
