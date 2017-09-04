# Given a triangle, find the minimum path sum
# from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#记忆搜索法
class Solution(object):
    memo = []
    def finmin(self,triangle,m,k):#当前点的最短 路径
        if(m == 0):
            self.memo[m][k] = triangle[0][0]
            return triangle[0][0]
        elif(k == 0):
            if(self.memo[m-1][k] != 'a'):
                self.memo[m][k] = triangle[m][k] + self.memo[m-1][k]
                return triangle[m][k] + self.memo[m-1][k]
            else:
                self.memo[m][k] = triangle[m][k] + self.finmin(triangle,m-1,k)
                return self.memo[m][k]
        elif(k == m):
            if (self.memo[m - 1][k-1] != 'a'):
                self.memo[m][k] = triangle[m][k] + self.memo[m - 1][k-1]
                return triangle[m][k] + self.memo[m - 1][k-1]
            else:
                self.memo[m][k] = triangle[m][k] + self.finmin(triangle,m-1,k-1)
                return self.memo[m][k]
        else:
            if(self.memo[m-1][k] == 'a'):
                self.memo[m-1][k] = self.finmin(triangle,m-1,k)
            if (self.memo[m - 1][k-1] == 'a'):
                self.memo[m-1][k-1] = self.finmin(triangle,m-1,k-1)
            self.memo[m][k] = triangle[m][k] + min(self.memo[m-1][k],self.memo[m-1][k-1])
            return self.memo[m][k]



    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #递归找
        self.memo = [['a' for i in j] for j in triangle]
        mins = 100000
        m  = len(triangle) -1   #最后一层
        k = 0 #最后一层开始找  每层的点
        # s = triangle[m][k]
        while(k < len(triangle[m]) ):
            s = self.finmin(triangle,m,k)
            mins = min(mins,s)
            k += 1
        print(self.memo)
        return mins


n = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
# print(n)
# print(len(n))
a = Solution().minimumTotal(n)

print(a)