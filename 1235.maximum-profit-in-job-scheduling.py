#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start

import bisect
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        A = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        A.sort()
        S = [a[0] for a in A]

        @cache
        def f(i):
            if i == n:
                return 0

            drop = f(i + 1)
            j = bisect.bisect_left(S, A[i][1])

            return max(drop, A[i][2] + f(j))

        n = len(A)
        return f(0)


# @lc code=end
