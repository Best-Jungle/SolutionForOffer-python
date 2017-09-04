# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        recor = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if ( recor.__contains__(k) ):
                return recor.get(k),i
            else:
                recor[nums[i]] = i

# nums = [3,3]
# print( Solution().twoSum(nums,6) )
a = {3:0}
print(a.get(0))
