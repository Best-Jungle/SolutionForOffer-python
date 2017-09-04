#For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minl = len(nums) + 1 #取一个不能取到的最长值，每次找最小
        head , end = 0 , -1 #为什么不能取0，0会越界，
        sum = 0
        while(head < len(nums)):
            if(sum < s and end < len(nums)- 1 ):
                end += 1
                sum += nums[end]

            else:
                sum -= nums[head]
                head += 1
            if (sum >= s):
                minl = min(end-head+1,minl)
        if(minl == len(nums)+1):
            return 0
        else:
            return minl





nums = [2,3,1,2,4,3]
print(len(nums))
a = Solution().minSubArrayLen(7,nums)
print(a)

# minl = len(nums) + 1  # 设置超出边界的值用于未来选小值
# top, end = 0, -1  # 开始滑动窗口里没有值，针对输入空列表时
# sum = 0
# while (top < len(nums) - 1):
#     if (sum < s and end < len(nums) - 1):
#         end += 1
#         sum += nums[end]
#     elif:
#         sum -= nums[top]
#         top += 1
#     if (sum >= s):
#         minl = min(end - top + 1, minl)
# if (minl == len(nums) + 1):
#     return 0
# else:
#     return minl