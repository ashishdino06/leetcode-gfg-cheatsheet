
class Solution:
    def findFloor(self, arr, x):
        # code here
        ans=-1
        l,h=0,len(arr)-1
        while l<=h:
            mid= l + (h-l)//2
            
            if arr[mid]>x:
                h=mid-1
            else:
                ans = mid
                l = mid+1
        return ans
