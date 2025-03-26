You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s can be formed by concatenating one or more words from the dictionary[].

Note: From dictionary[], any word can be taken any number of times and in any order.

Examples :

Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
Output: true
Explanation: s can be breakdown as "i like".
Input: s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: true
Explanation: s can be breakdown as "i like gfg".
Input: s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: false
Explanation: s cannot be formed using dictionary[] words.
Constraints:
1 ≤ s.size() ≤ 3000
1 ≤ dictionary.size() ≤ 1000
1 ≤ dictionary[i].size() ≤ 100

# Solution:
class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        st = set(dictionary)
        l, n = len(max(dictionary, key=len)), len(s)

        dp = [False]*(n+1)
        dp[0] = True
        
        for j in range(n):
            for i in range(j, max(-1, j-l), -1):
                dp[j+1] = dp[j+1] or dp[i] and (s[i:j+1] in st)

        return dp[-1]
