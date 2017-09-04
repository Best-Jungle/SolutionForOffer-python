def maxmoney(m,n,a,b,c,d,x,y,z):
    mam = 0
    money = 0
    m1 = m//b
    n1 = n//a
    if(m1 < n1):
        l = m1
    else:
        l = n1
    for i in range(l+1):
        money = y*((m - i*b)//c)+z*((n - i*a)//d)+i*x
        mam = max(mam,money)
    return mam

a1 = []
a2 = []
a3 = []
s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
# s1 = input()
# s2 = input()
# s3 = input()
# raw_input()里面不要有任何提示信息
for x in s1.split():
    a1.append(int(x))
for x in s2.split():
    a2.append(int(x))
for x in s3.split():
    a3.append(int(x))

n,m = a1[0],a1[1]
a,b,c,d = a2[0],a2[1],a2[2],a2[3]
x,y,z = a3[0],a3[1],a3[2]

# n,m = 5,5
# a,b,c,d = 1,2,3,3
# x,y,z = 2,1,3
print(maxmoney(m,n,a,b,c,d,x,y,z))
