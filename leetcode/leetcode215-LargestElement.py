# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ? k ? array's length.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


#方法1
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         a,b = -1,len(nums)-1
#         while(a != len(nums)-k):
#             if(a > len(nums)-k):
#                 a,b = 0,a-1
#             else:
#                 a,b = a+1,len(nums)-1
#             a = self.position(a, b, nums)
#
#         print(nums[a])
#
#     def position(self,a,b,nums):
#         k = nums[a]
#         while(a<b):
#             while(nums[b]>=k and a<b):
#                 b -= 1
#             if(a<b):
#                 nums[a] = nums[b]
#             while(nums[a]<=k and a<b):
#                 a += 1
#             if(a<b):
#                 nums[b] = nums[a]
#         nums[a] = k
#         return a

import heapq


class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]

    def findKthLargest(self, nums, k):
        if len(nums) == 0:
            return None

        self.quickselect(nums, k, 0, len(nums) - 1)
        print(sorted(nums[:k])[0])
        return sorted(nums[:k])[0]

    def quickselect(self, nums, k, start, end):
        if start == end:
            return
        if start >= k or end < k:
            return

        left = start
        right = end

        pivot = nums[left]

        while left < right:

            while left < right and nums[right] <= pivot:
                right -= 1
            nums[left] = nums[right]

            while left < right and nums[left] >= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        self.quickselect(nums, k, start, left - 1)
        self.quickselect(nums, k, left + 1, end)

s = Solution()
nums = [3,2,1,5,6,4]
nums1 = [2,1]
s.findKthLargest(nums1,2)



