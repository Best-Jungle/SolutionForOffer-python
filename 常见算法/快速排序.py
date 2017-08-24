def position(nums,low, high):#返回排序完位置,一次快排
    # k = nums[low] #第一种方法
    # while(low<high):
    #     while(k <= nums[high] and low <high):
    #         high -= 1
    #     if ( low < high ):
    #         nums[low] , nums[high] = nums[high] , nums[low]
    #     while(low < high and k >= nums[low]):
    #         low += 1
    #     if(low<high):
    #         nums[low] , nums[high] = nums[high] , nums[low]
    # return low

    #第二种方法
    key = nums[low]
    while( low < high ):
        while(low < high and nums[high] >= key):
            high -= 1
        while(low < high and nums[high] <= key):
            nums[low] = nums[high]
            low += 1
            nums[high] = nums[low]
    nums[low] = key
    return low





def quick_sort(nums,low,high):#快排
    if(low<high):
        p = position(nums,low,high)
        quick_sort(nums,low,p-1)
        quick_sort(nums,p+1,high)
a = [3,3,4,1,2,6,8,7,9]
b = [19,8,11,6,5,4,3,22,12]
quick_sort(b,0,len(b)-1)
print(b)