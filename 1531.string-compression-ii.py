#
# @lc app=leetcode id=1531 lang=python3
#
# [1531] String Compression II
#

# @lc code=start

import math
from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class State:
    letter: int
    consecute: int
    total: int


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        S: dp[i][budget][c][ccnt]:
            index i onwards, remaining budget to delete, next letter c, consecutive count for letter c
        """

        @cache
        def f(i: int, budget: int, c: str, ccnt: int) -> int:
            if budget < 0:
                return math.inf

            if i == n:
                return 0

            if s[i] == c:
                # No need to delete since there is state
                # Keep
                inc = 1 if ccnt in (1, 9, 99) else 0
                return inc + f(i + 1, budget, c, ccnt + 1)
            else:
                # Delete
                delete = f(i + 1, budget - 1, c, ccnt)
                keep = 1 + f(i + 1, budget, s[i], 1)

                return min(keep, delete)

        n = len(s)

        return f(0, k, "", 0)


# @lc code=end
