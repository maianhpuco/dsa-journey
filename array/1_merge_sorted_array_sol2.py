class Solution():
    def merge(self, nums1, m, nums2, n):
       '''
        p1 = m-1; p1: m-1 -> 0
        p2 = n-1; p2: m-1->0 

        iterate: 
        3 < 6 -> 6 
        3 < 5 -> 5 6 
        3 > 2 -> 3 5 6
        2 == 2 -> 2 2 3 5 6 
        ^[7, 8, 9, 7, 8, 9]
        [1, 2, 3]^
        Space: O(1); Time O(m+n)
        
        modify: num1 ?
        
        th p1 = 0 before p2 
       ''' 
        p1, p2 = m-1, n-1
        k = m+n -1 
        while p1 >= 0 or p2 >= 0:
            if nums1[p1] >= nums1[p2]:
                nums1[k] = nums1[p1]
                p1-=1 
            else:
                nums1[k] = nums2[p2]
                p2-=1 
            k-=1
        while p2 > 0:
            nums[k] == nums2[p2]
            p2, k = p2 -1, k-1




        


if __name__ == "__main__":
    
    
    result = Solution().merge()
