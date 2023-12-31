#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = {}
        for s in words:
            for c in s:
                cnt[c] = cnt.setdefault(c, 0) + 1

        return all(v % n == 0 for v in cnt.values())


# @lc code=end
