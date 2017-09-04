# import heapq
# def maxSubArray(nums):#暴力解法
#     s = []
#     for i in range(len(nums)):
#         s.append(nums[i])
#         key = nums[i]
#         for j in nums[i+1:]:
#             key = key + j
#             s.append(key)
#     return heapq.nlargest(1,s).pop()



# def maxSubArray(nums):#暴力解法
#     mam = -10000
#     for i in range(len(nums)):
#         s = nums[i]
#         for j in range(i+1,len(nums)):
#             mam = max(s,mam)
#             s += nums[j]
#     return mam

def maxSubArray(nums):#动态规划
    maxsum = 0 #总和
    maxtmp = 0 #游标
    for i in range(len(nums)):
        if( maxtmp < 0 ):
            maxtmp = nums[i]
        else:
            maxtmp += nums[i]
        maxsum = max(maxtmp,maxsum)

    return maxsum




nums = [-3,-2,-4,-200,-83,-21,-33]
print(maxSubArray(nums))