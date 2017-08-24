def Solution(nums):
    change = 0
    one, i, three = -1, 0, len(nums)
    while (i < three):
        if (nums[i] == 1 ):
            one += 1
            nums[one], nums[i] = nums[i], nums[one]
            if(nums[one]!=nums[i]):
                change += 1
            i += 1
        elif (nums[i] == 3):
            three -= 1
            nums[three], nums[i] = nums[i], nums[three]
            if(nums[three]!= nums[i]):
                change += 1
        else:
            i += 1
    return change

# nums = [2,2,1,3,3,3,2,3,1]
n = int(input())
for i in range(n):
    nums.append(int(input()))
a = Solution(nums)
print(a)


