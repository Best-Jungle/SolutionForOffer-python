# For example, given array ,
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#暴力解法
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        record = {}
        x = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (record.__contains__((i,j,k))) :
                        continue
                    elif( nums[i] + nums[j] + nums[k] == 0):
                        r = (i,j,k)
                        record[(i,j,k)] = x
                        x += 1

S = [-1, 0, 1, 2, -1, -4]
a = Solution().threeSum(S)
print(a)