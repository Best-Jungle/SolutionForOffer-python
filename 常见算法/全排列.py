COUNT = 0
def prem(nums,begin,end):
    global COUNT
    if(begin>=end):
        print(nums)
        COUNT += 1
    else:
        i = begin
        for n in range(begin,end):
            nums[n], nums[i] = nums[i], nums[n]
            prem(nums,begin+1,end)
            nums[n] , nums[i] = nums[i] ,nums[n]

nums = [1,2,3,4]
prem(nums,0,len(nums))
print(COUNT)
