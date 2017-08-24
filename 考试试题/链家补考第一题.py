def mean1(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/(len(nums))
def mean2(n_mean,l,n):
    return (n_mean*l + n)/(l+1)

def position(nums,low, high):
    key = nums[low]
    while( low < high ):
        while(low < high and nums[high] >= key):
            high -= 1
        while(low < high and nums[high] <= key):
            nums[low] = nums[high]
            low += 1
            nums[high] = nums[low]
    nums[low] = key
    return low

def quick_sort(nums,low,high):#快排
    if(low<high):
        p = position(nums,low,high)
        quick_sort(nums,low,p-1)
        quick_sort(nums,p+1,high)

def Solution(nums,mums):
    number = 0
    l = len(nums)
    nums_mean = mean1(nums)
    mums_mean = mean1(mums)
    quick_sort(mums,0,len(mums)-1)
    while(mums[-1] != mums[0]):
        if(mums[-1] < nums_mean):
            return number
        elif(mums[-1] > nums_mean):
            n = mums.pop()
            nums_mean = mean2(nums_mean,l,n)
            number += 1
    return number

N = int(input())
n = input()
nums = [int(x) for x in n.split()] #数学
M = int(input())
m = input()
mums = [int(x) for x in m.split()]#计算机
# nums = [3,2,3]
# mums = [3,2,5]
a = Solution(nums,mums)
print(a)


