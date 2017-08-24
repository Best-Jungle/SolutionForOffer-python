def BinarySearch(nums,key):
    l,r = -1 , len(nums)
    while(l<r):
        k = (r+l)//2
        if (nums[k] == key):
            return k
        elif(nums[k] > key):
            r = k
        else:
            l = k
    return


nums = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(nums,5))

