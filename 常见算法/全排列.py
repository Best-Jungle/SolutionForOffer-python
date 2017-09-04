# COUNT = 0
# def prem(nums,begin,end):
#     global COUNT
#     if(begin>=end):
#         print(nums)
#         COUNT += 1
#     else:
#         i = begin
#         for n in range(begin,end):
#             nums[n], nums[i] = nums[i], nums[n]
#             prem(nums,begin+1,end)
#             nums[n] , nums[i] = nums[i] ,nums[n]
count = 0
def prem(nums,head,end):
    global count
    if( head >= end):
        count += 1
        print(nums)
    for i in range(head,end):
        nums[head],nums[i] = nums[i],nums[head]
        prem(nums,head+1,end)
        nums[head],nums[i] = nums[i],nums[head]




nums = [1,2,3,4]
prem(nums,0,len(nums))
print(count)
