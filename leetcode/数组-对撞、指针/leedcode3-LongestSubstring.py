#滑动窗口法 ,求最长不重复序列
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         nums = [0 for i in range(256)]
#         head , end = 0 , -1
#         l = 0
#         string = ''
#         while( head < len(s) ):
#             if ( end < len(s)-1 and nums[ord(s[end+1])] == 0): #注意 and 的位置
#                 end += 1
#                 nums[ord(s[end])] = 1
#             else:
#                 nums[ord(s[head])] = 0
#                 head += 1
#
#             l = max(l,end-head+1)
#         return l

#第二种！
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        right = 0
        maxlen = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                maxlen = max(maxlen, right - left + 1)
            else:
                while s[right] in seen:
                    if s[left] == s[right]:
                        left += 1
                        break
                    else:
                        seen.remove(s[left])
                        left += 1
            right += 1
        return maxlen

s = "abcabcbb"
print(len(s))

a = Solution().lengthOfLongestSubstring(s)
print(a)


