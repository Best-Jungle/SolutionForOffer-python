# 输入
# x = input()
# nums = [int(n) for n in x.split()]
# n , m = nums[0] , nums[1]
# x = input()
# nums = [int(n) for n in x.split()]

def findNum(array, n, m):
    res = array[0]
    nums = []
    for i in range(n/m+1):
        nums = nums + array
    m = len(nums)
    if array[0] > 1:
        for i in range(m):
            k = res[i]
            if i == 0:
                k -= 1
            for j in range(k):
                res.append(nums[i])
    else:
        res.append(array[1])
        for i in range(1, m):
            k = res[i]
            if i == 1:
                k -= 1
            for j in  range(k):
                res.append(nums[i])
    for i in range(n):
       print res[i]

# n, m = map(int, raw_input().split())
# nums = map(int, raw_input().split())
n , m = 30 , 4
nums = [2,1,3,1]
findNum(nums,n,m)