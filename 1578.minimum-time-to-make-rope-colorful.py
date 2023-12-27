#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start


from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        curr, ret, n = 0, 0, len(colors)

        while curr < n:
            max_time, color = neededTime[curr], colors[curr]

            tot_time = max_time
            i = curr
            while i + 1 < n and colors[i + 1] == color:
                tot_time += neededTime[i + 1]
                max_time = max(max_time, neededTime[i + 1])

                i += 1

            ret += tot_time - max_time
            curr = i + 1

        return ret


# @lc code=end
