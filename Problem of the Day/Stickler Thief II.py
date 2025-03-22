You are given an array arr[] which represents houses arranged in a circle, where each house has a certain value. A thief aims to maximize the total stolen value without robbing two adjacent houses.
Determine the maximum amount the thief can steal.

Note: Since the houses are in a circle, the first and last houses are also considered adjacent.

Examples:

Input: arr[] = [2, 3, 2]
Output: 3
Explanation: arr[0] and arr[2] can't be robbed because they are adjacent houses. Thus, 3 is the maximum value thief can rob.
Input: arr[] = [1, 2, 3, 1]
Output: 4
Explanation: Maximum stolen value: arr[0] + arr[2] = 1 + 3 = 4
Input: arr[] = [2, 2, 3, 1, 2]
Output: 5
Explanation: Maximum stolen value: arr[0] + arr[2] = 2 + 3 = 5 or arr[2] + arr[4] = 3 + 2 = 5
Constraints:
2 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104

# Solution:
class Solution:
    def maxValue(self, arr):
        def f(ind, dp, arr):
            if ind >= len(arr):
                return 0
            if ind in dp:
                return dp[ind]
            p1 = arr[ind] + f(ind + 2, dp, arr)
            p2 = f(ind + 1, dp, arr)
            dp[ind] = max(p1, p2)
            return dp[ind]

        if not arr:
            return 0

        n = len(arr)
        dp1, dp2 = {}, {}
        v1, v2 = arr[:-1], arr[1:]

        f1 = f(0, dp1, v1)
        f2 = f(0, dp2, v2)

        return max(f1, f2)
