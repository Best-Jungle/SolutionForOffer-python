# def Sort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j][1] > nums[j+1][1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
# a = [[1,2],[1,3],[1,1]]
# print(Sort(a))
num = [2,2,3,4,5,6]
num = list(set(num))
for i in range(2,4):
    print(i)