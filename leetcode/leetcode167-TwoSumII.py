#给一个子序列 和一个数，返回相加得到该数的序号
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l , r = 0 , len(numbers)-1
        while(l<r):
            k = numbers[l] + numbers[r]
            if(k==target):
                return l+1,r+1
            if(k<target):
                l += 1
            else:
                r -= 1
        return "The input has no solution"

target = 9
nums = [1,2,7,9]
# a = Solution()
# print(a.twoSum(nums,target))
Solution().twoSum(nums,target)