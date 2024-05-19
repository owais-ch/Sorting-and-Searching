'''

Given a binary sorted non-increasing array of 1s and 0s. You need to print the count of 1s in the binary array.

Example 1:

Input:
N = 8
arr[] = {1,1,1,1,1,0,0,0}
Output: 5
Explanation: Number of 1's in given 
binary array : 1 1 1 1 1 0 0 0 is 5.
Example 2:

Input:
N = 8
arr[] = {1,1,0,0,0,0,0,0}
Output: 2
Explanation: Number of 1's in given 
binary array : 1 1 0 0 0 0 0 0 is 2.
'''

class Solution:
    ##Complete this code
    def countOnes(self,arr, n):
        low,high=0,n-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==1:
                if mid+1>=n:
                    return n
                if arr[mid+1]==0:
                    return mid+1
                elif arr[mid+1]==1:
                    low=mid+1
            elif arr[mid]==0:
                if mid-1<0:
                    return mid
                elif arr[mid-1]==1:
                    return mid
                elif arr[mid-1]==0:
                    high=mid-1
