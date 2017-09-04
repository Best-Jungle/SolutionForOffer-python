
n = 5
a2 =[4,5,1,3,2]

memo = [0 for i in range(n)] #记录的是前面比它大的数
l = 0
while(l<len(a2)):
    s = 0
    k = l - 1
   while(k>=0):
       if(a2[l] < a2[k]):
           s += memo[k] + 1



