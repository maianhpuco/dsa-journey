# link : https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        max_length = float('-inf')

        for right in range(n):

            # change window when : meet a duplicated character
            while s[right] in s[left:right]:
                max_length = max(max_length, right + 1 - left -
                                 1)  # update when meet duplicated character
                left += 1
        if max_length == float('-inf'):
            max_length = n
        else:
            max_length = max(max_length,
                             right + 1 - left)  # update when end of string
        return max_length
