# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
class Solution(object):
    def sortColors(self, nums):
        zero,i,two = -1,0,len(nums)
        while(i<two):
            if(nums[i] == 0 ):
                zero += 1
                nums[zero],nums[i] = nums[i],nums[zero]
                i +=1
            elif(nums[i] ==2):
                two -= 1
                nums[two],nums[i] = nums[i],nums[two]
            else:
                i += 1
        print(i)

a = Solution()
b = [0,1,2,1,0,2,0,1,0,2,1,0]
a.sortColors(b)


