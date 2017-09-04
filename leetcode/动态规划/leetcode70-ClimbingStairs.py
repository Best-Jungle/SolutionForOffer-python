#爬 n 阶楼梯，一次爬一格或者2格，有多少种爬法
class Solution(object):
    # def climb(self,n):
    #     # print(self.memory)
    #     if(n==0 or n==1):
    #         return 1
    #     if(self.memory[n] == -1):
    #         self.memory[n] = self.climb(n-1)+self.climb(n-2)
    #     return self.memory[n]


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1.递归的方法
        # if(n == 1 or n == 0):
        #     return 1
        # if(n == 2):
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        #
        #2.记忆搜索法
        # self.memory = [-1 for i in range(n+1)]
        # return self.climb(n)

        # 2.动态规划法
        memory = [-1 for i in range(n+1)]
        memory[0] = 1
        memory[1] = 1
        for i in range(2,n+1):
            memory[i] = memory[i-1] + memory[i-2]
        return memory[n]



a = Solution().climbStairs(10)
print(a)