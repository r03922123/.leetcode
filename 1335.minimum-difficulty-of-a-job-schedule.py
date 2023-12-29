#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
import math
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def f(i: int, budget: int, prev_max: int) -> int:
            """Return best job difficulty consider following args as a state

            Args:
                i (int): started from index i onwards for
                budget (int): remaining budget days for arrangement
                prev_max (int): job difficulty at last day

            Returns:
                int: min difficulty consider the given state
            """
            if i == n:
                if budget == 0:
                    return prev_max

                return math.inf

            if budget < 0:
                return math.inf

            # Remaining tasks cannot less than number of budget days
            remain_task = (n - 1) - i + 1
            if remain_task < budget:
                return math.inf

            # Two choices
            # END: use current task as starting task on a new day
            end = prev_max + f(i + 1, budget - 1, jobDifficulty[i])
            # MIXED: merge current task to last day
            mix = f(i + 1, budget, max(prev_max, jobDifficulty[i]))

            return min(end, mix)

        n = len(jobDifficulty)
        ret = f(0, d, 0)
        return ret if ret < math.inf else -1


# @lc code=end
