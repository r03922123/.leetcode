#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start

from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        ret = []
        for a in nums:
            counter[a] = counter.setdefault(a, 0) + 1

            if counter[a] > len(ret):
                ret.append([])

            ret[counter[a] - 1].append(a)

        return ret


# @lc code=end
