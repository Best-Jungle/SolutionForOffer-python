class Solution(object):
	def method(self,nums):
		y = 0
		for x in range(len(nums)):
			if nums[x]:
				nums[x], nums[y] = nums[y], nums[x]
				y += 1
		print(nums)
nums = [1, 0, 3, 4, 0, 6]
a = Solution()
a.method(nums)



# class Solution(object):
# 	def method(self):
# 		print("ok")
# nums = [1, 0, 3, 4, 0, 6]
# a = Solution()
# a.method()