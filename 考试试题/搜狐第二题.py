#输入
# zero = [0 for i in range(6)]
# nums = []
# num = []
# i = 0
# while(num != zero ):
#     x = input()
#     num = [int(n) for n in x.split()]
#     nums[i] = num
#     i += 1
def Soulution( nums ):
    bag = []
    for i in range(len(nums)-1):
        b = nums[i][5]
        l , r = 0 , 4
        while(l < = r):
            if ( nums[i][r] > 0):
                if(l == r):
                    b += 6//nums[i][r]
                    nums[i][r] = nums[i][r]%2
                    break
                if(nums[i][r] >= nums[i][l]):
                    b += nums[i][r]
                    nums[i][l] , nums[i][r] = 0,0
                    l += 1
                    r -= 1
                elif(nums[i][r] < nums[i][l]):
                    b += nums[i][r]
                    nums[i][r] = 0
                    nums[i][l] -= nums[i][r]
                    l += 1
                    r -= 1
        if(nums[i][3] > 0):
            if(nums[i][0] > 0):
                b += nums[i][3]
                if(nums[i][0] - nums[i][3] > 0):









nums = [[0,0,4,0,0,1],[7,5,1,0,0,0],[0,0,0,0,0,0]]#测试数据
a = Soulution(nums)
print(a)


