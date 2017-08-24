def Soulution():
    x = input()
    num = [int(n) for n in x.split()]
    x,f,d,p = num[0],num[1],num[2],num[3]
    if(x*f>=d):
        day = d//x
        return day
    else:
        day , money = f , d - x*f
        k = x+p
        day = money//k+f
        return day

a = Soulution()
print(a)

