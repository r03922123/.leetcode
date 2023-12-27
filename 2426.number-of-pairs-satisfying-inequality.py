#
# @lc app=leetcode id=2426 lang=python3
#
# [2426] Number of Pairs Satisfying Inequality
#

# @lc code=start


from typing import List, Tuple


class Solution:
    def numberOfPairs(
        self, nums1: List[int], nums2: List[int], diff: int
    ) -> int:
        diff_arr = [a - b for a, b in zip(nums1, nums2)]
        # check how many pair s.t. diff[i] - diff[j] <= diff
        return self.merge_sort(diff_arr, 0, len(diff_arr) - 1, diff)[1]

    def merge(self, left: List[int], right: List[int]):
        ret = []
        pl = pr = 0
        while pl < len(left) and pr < len(right):
            if left[pl] < right[pr]:
                ret.append(left[pl])
                pl += 1
            else:
                ret.append(right[pr])
                pr += 1

        while pl < len(left):
            ret.append(left[pl])
            pl += 1

        while pr < len(right):
            ret.append(right[pr])
            pr += 1

        return ret

    def merge_sort(
        self, diff_arr: List[int], i: int, j: int, diff: int
    ) -> Tuple[List[int], int]:
        """Sort arr[i->j] using merge sort

        Args:
            i (int): start pointer
            j (int): end pointer

        Returns:
            Tuple[List[int], int]: Sorted arr[i->j] and number of valid pair in arr[i->j]
        """

        if i == j:
            return [diff_arr[i]], 0

        mid = (i + j) // 2

        left, cntL = self.merge_sort(diff_arr, i, mid, diff)
        right, cntR = self.merge_sort(diff_arr, mid + 1, j, diff)

        # =========================== #
        # Two Pointer
        # Count the valid pairs, (left and right are sorted in increasing order)
        # IF left[l] - right[r] <= diff
        #   left[0->l] - right[r] <= diff, number of pairs is l + 1
        #   search r instead
        #   Move r -> r - 1
        # ELSE
        #   left[0->l] - right[r] > diff
        #   search possible l s.t. left[l] - left[r] is smaller
        #   Move l -> l - 1

        # pl, pr = len(left) - 1, len(right) - 1
        # while pl >= 0 and pr >= 0:
        #     if left[pl] - right[pr] > diff:
        #         pl -= 1
        #     else:
        #         cntT += pl + 1
        #         pr -= 1
        # =========================== #

        # =========================== #
        # Sliding Window
        pl = cntT = 0
        for pr in range(len(right)):
            while pl < len(left) and left[pl] - right[pr] <= diff:
                pl += 1

            cntT += pl
        # =========================== #

        ret = self.merge(left, right)
        return ret, cntT + cntL + cntR


# @lc code=end
