n = 123456
nlen=len(str(n))

def reverse(n):
    x=0
    for i in range(nlen):
        residu = n % 10
        n = n // 10
        x += residu
        x = x*10
    x = x //10
    return x

print(reverse(n))