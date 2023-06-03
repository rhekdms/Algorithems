d={0:0,1:1}
def f(n):
    if n in d:
        return d[n]
    o=f(n-1)+f(n-2)
    d[n]=o
    return o
print(f(int(input())))