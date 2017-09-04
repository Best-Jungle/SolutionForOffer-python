#求连续子串最大和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = g = -1000000000
        for n in nums:
            l = max(n,l+n)
            g = max(l,g)
        return g
# x = input()
# nums = [int(n) for n in x.split()]
nums = [-3,-2,-10,-200,-83,-21,-33]
a = Solution().maxSubArray(nums)
print(a)