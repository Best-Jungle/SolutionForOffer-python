# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # index = 0
        # for num in nums:
        #     if num != val:
        #         nums[index] = num
        #         index += 1
        # for i in range(len(nums)-index):
        #     nums.pop()
        # print(nums)
        # return index

        # 方法二
        start,end = 0,len(nums)-1
        if nums!=[]:
            while start != end :
                if nums[start] == val:
                    nums[start],nums[end] = nums[end],nums[start]
                    end -= 1
                else:
                    start +=1
        print (nums)
        return  start

a = Solution()
nums = [3,2,2,3]
a.removeElement(nums,2)