#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # [2 2 2 2 2] -> (3, 2)
        # [2 2 2 2] -> (2, 2)

        ret = 0
        counter = Counter(nums)
        for v in counter.values():
            if v == 1:
                return -1

            # Get the ceil(v / 3)
            ret += (v + 2) // 3

        return ret


# @lc code=end
