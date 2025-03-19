In the stock market, a person buys a stock and sells it on some future date. You are given an array prices[] representing stock prices on different days and a positive integer k, find out the maximum profit a person can make in at-most k transactions.

A transaction consists of buying and subsequently selling a stock and new transaction can start only when the previous transaction has been completed.

Examples :

Input: prices[] = [10, 22, 5, 80], k = 2
Output: 87
Explaination:
1st transaction: Buy at 10 and sell at 22. 
2nd transaction : Buy at 5 and sell at 80.
Total Profit will be 12 + 75 = 87.
Input: prices[] = [20, 580, 420, 900], k = 3
Output: 1040
Explaination: 
1st transaction: Buy at 20 and sell at 580. 
2nd transaction : Buy at 420 and sell at 900.
Total Profit will be 560 + 480 = 1040.
Input: prices[] = [100, 90, 80, 50, 25],  k = 1
Output: 0
Explaination: Selling price is decreasing continuously
leading to loss. So seller cannot have any profit.
Constraints:
1 ≤ prices.size() ≤ 103
1 ≤ k ≤ 200
1 ≤ prices[i] ≤ 103

# Solution:
class Solution:
    def maxProfit(self, prices, k):
        # code here
        n = len(arr)
        if k == 0 or n < 2:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if arr[i] > arr[i - 1]:
                    profit += arr[i] - arr[i - 1]
            return profit
        else:
            prev_dp = [0] * n
            for t in range(1, k + 1):
                curr_dp = [0] * n
                max_diff = -arr[0]
                for i in range(1, n):
                    curr_dp[i] = max(curr_dp[i - 1], arr[i] + max_diff)
                    max_diff = max(max_diff, prev_dp[i] - arr[i])
                prev_dp = curr_dp.copy()
            return prev_dp[-1]
