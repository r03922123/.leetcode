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
        @cache
        def f(i: int, budget: int, last_c: str, ccnt: int) -> int:
            """Return best result consider following arguments as a state

            Args:
                i (int): started from index i onwards for creating implicit string builder
                budget (int): remaining budget to delete
                last_c (str): last letter c in the string bulder considered before index i
                ccnt (int): consecutive count for letter last_c

            Returns:
                int: optimal compression length
            """
            if budget < 0:
                return math.inf

            if i == n:
                return 0

            if s[i] == last_c:
                # No need to take "Delete" choice since there are same states
                # result in same encoding results
                # generated by "Delete" in the ELSE Branch s[i] != c

                # Keep
                inc = 1 if ccnt in (1, 9, 99) else 0
                return inc + f(i + 1, budget, last_c, ccnt + 1)
            else:
                # Delete
                delete = f(i + 1, budget - 1, last_c, ccnt)
                # Keep
                keep = 1 + f(i + 1, budget, s[i], 1)

                return min(keep, delete)

        n = len(s)

        return f(0, k, "", 0)


# @lc code=end
