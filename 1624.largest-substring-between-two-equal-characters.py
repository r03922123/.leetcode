#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        start_idx = {}
        ret = -1
        for i, c in enumerate(s):
            ret = max(i - start_idx.setdefault(c, i + 1), ret)

        return ret


# @lc code=end
