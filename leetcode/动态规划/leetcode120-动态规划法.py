#动态规划法

class Solution(object):


    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #动态规划
        if(len(triangle) == 1):
            return triangle[0][0]
        self.memo = [['a' for i in j] for j in triangle]
        mins = 100000 #存放最短路径
        m  = 1   #层数
        k = 0 #每层的点
        # s = triangle[m][k]
        self.memo[0][0] = triangle[0][0]
        while( m < len(triangle)):
            k = 0
            while(k<len(triangle[m])):
                if(k == 0):
                    self.memo[m][k] = triangle[m][k] + self.memo[m-1][k]
                elif(k == m):
                    self.memo[m][k] = triangle[m][k] + self.memo[m-1][k-1]
                else:
                    self.memo[m][k] = triangle[m][k] + min(self.memo[m-1][k-1],self.memo[m-1][k])
                if (m == len(triangle) - 1 ):
                    mins = min(mins,self.memo[m][k])
                k += 1
            m += 1
        return mins

    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        currLv = triangle[len(triangle) - 1]
        for i in reversed(range(len(triangle) - 1)):
            affectedLv = triangle[i]
            for j in range(len(affectedLv)):
                affectedLv[j] += min(currLv[j], currLv[j + 1])
            currLv = affectedLv
        return triangle[0][0]


n = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

a = Solution().minimumTotal1(n)
print(a)