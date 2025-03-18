Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.

Note: Each element must be in exactly one subset.

Examples:

Input: arr = [1, 5, 11, 5]
Output: true
Explanation: The two parts are [1, 5, 5] and [11].
Input: arr = [1, 3, 5]
Output: false
Explanation: This array can never be partitioned into two such parts.
Constraints:
1 ≤ arr.size ≤ 100
1 ≤ arr[i] ≤ 200

# Solution:
class Solution:
    
    def f(self,arr,size,index,s,current,dp):
        if current ==(s/2):
            return 0
        if index >size -1 :
            return float('inf')
        ans=float('inf')
        #take cndn  
        if dp [index][current]!=-1:
            return dp[index][current]
        if (current +arr[index]) < s:
            ans = self.f(arr,size,index+1,s,current+arr[index],dp)
        if ans==0:
            return 0
        #not take cndn 
        ans=self.f(arr,size,index+1,s,current,dp)
        dp[index][current]= ans
        return dp[index][current]
    
    def equalPartition(self, arr):
        size =len (arr)
        s=0
        for i in range (size):
            s+=arr[i]
        dp = [[-1]*(s+1) for i in range (size)]    
        ans =self.f(arr,size,0,s,0,dp)
        if (ans==0):
            return True 
        return False
