def Sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j][1] > nums[j+1][1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
def Solution(n,r,avg,d):
    if(n == 0 or r == 0 or avg == 0):
        return
    else:
        sum = avg * n
        sum_now = 0
        d = Sort(d)
        for i in range(n):
            sum_now += d[i][0]
        de = sum - sum_now
        k = 0
        time = 0
        while(de!=0 and k < n-1):
            if(d[k][0] < 5):
                time += d[k][1]
                d[k][0] += 1
                de -= 1
            else:
                k += 1
        return time

x = input()
num = [int(l) for l in x.split()]
n,r,avg = num[0],num[1],num[2]
d = []
for i in range(n):
    x = input()
    c = [int(l) for l in x.split()]
    d.append(c)
time = Solution(n,r,avg,d)
print(time)



