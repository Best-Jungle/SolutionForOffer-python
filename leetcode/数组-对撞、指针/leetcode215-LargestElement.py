#找到数组中第 k 大个数
import heapq
class Solution(object):
    def positon(self,nums,l,r):
        k = nums[l]
        while(l<r):
            while(nums[r] > k):
                r -= 1
            while(nums[r] <= k and l<r):
                nums[l] = nums[r]
                l += 1
                nums[r] = nums[l]
        nums [l] = k
        return l


        return key
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l ,r = 0,len(nums)-1
        while(l <= r):
            p =  self.positon(nums,l,r)
            if(p < len(nums)-k):
                l = p+1
            elif(p > len(nums)-k):
                r = p - 1
            else:
                return nums[p]


nums = [3,2,10,200,83,21,33]
print(Solution().findKthLargest(nums,1))