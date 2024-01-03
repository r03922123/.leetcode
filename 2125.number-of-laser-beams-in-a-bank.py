#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # [3 0 3 4]
        ret = prev = 0
        for row in bank:
            curr = row.count("1")
            if curr:
                ret += curr * prev
                prev = curr

        return ret


# @lc code=end
