# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q = m-1,n-1
        while(p>=0 and q>=0):
            if(nums1[p]>nums2[q]):
                nums1[p+q+1] = nums1[p]
                p -=1
            else:
                nums1[p+q+1] = nums2[q]
                q -=1
        nums1[:q + 1] = nums2[:q + 1]
        print(nums1)

        print(nums1)

nums1 = [1, 2, 3, 4, 5, 6,0,0,0,0]
nums2 = [7, 8, 9, 10]
a = Solution()
a.merge(nums1, 6, nums2, 4)
print(nums1[0:2])
