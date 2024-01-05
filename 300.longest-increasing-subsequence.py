#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for a in nums:
            i = bisect.bisect_left(dp, a)
            if i == len(dp):
                dp.append(a)
            else:
                dp[i] = a

        return len(dp)


# @lc code=end
