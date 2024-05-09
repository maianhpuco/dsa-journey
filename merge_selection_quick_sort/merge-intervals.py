# link: https://leetcode.com/problems/merge-intervals/
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals = [[1,3],[2,6],[8,10],[15,18]] 
        output: [[1, 6],[8,10],[15,18]]

        overlap: start_1 end_1: 
        ---------------------x_axis 
        [.   ]
            [.     ]
             [.     ]
        [.          ]
          [] -> s_2 
        [1,3],[2,6] [s_1, e_1][s_2, e_2]
        compare: start_2 >= start_1 (this is a normal merge sort problem)
            -> if start_2 <= end_2:
                    then merge 
            -> else: not merge 

        def merge(arr1, arr2): start_2 <= end_2 
            #start of output: s_1
            #end: if e_2 < e_1 -> e_1 
                    else: e_1 hay là max(e_1, e_1)

        [[1,3][15,18]      | [2,6],[6,10]    ]
                             ^r 
        ^l   
        -> merge and merge interval 
        [1, 3][2,6][6,10] -> [1, 6, 10] 
        and merge interval
        TC: O(nlogn)
        SC: O(nlogn)
        '''

        def merge_interval(result2d, new_interval):  #merge taking 1
            '''
            2 scenario:
            [1, 3] vs [2, 5] or [3, 5] (in range)
            [1, 3] vs [4, 5] (out range)
            '''
            if result2d == []:
                result2d.append(new_interval)
            else:
                arr1 = result2d[-1]
                arr2 = new_interval
                if arr2[0] > arr1[1]:  # [1, 4][5, 6]
                    result2d.append(arr2)
                elif arr2[0] <= arr1[1] and arr2[1] >= arr1[
                        1]:  # [1, 4] vs [2, 5] -> return [1, 5]
                    result2d[-1][1] = arr2[1]
                else:  #arr2[0] <= arr1[1] and arr2[1] < arr1[1]:  # [1, 4] vs [2, 3]
                    pass

        #normal merge sort
        def merge_sort(array2d, left, right):
            '''
            left_side = [[1, 6]]  right_side = [[8, 10], [15, 18]] 
            [1, 6] 
            [[1, 6], [8, 10]] vs [[1, 6], [8, 10]] 
            [[1, 6], [8, 10], [15, 18]] 
            '''

            mid = left + (right - left) // 2
            if left == right:
                return array2d[left:right + 1]  #ex: [1,3]
            #divide step
            left_side = merge_sort(array2d, left, mid)  #divide taking O(logn)
            right_side = merge_sort(array2d, mid + 1, right)
            #merge step
            l, r = 0, 0
            result2d = []
            while l < len(left_side) and r < len(right_side):
                #merge operation
                if left_side[l][0] < right_side[r][0]:  #compare taking O(n)
                    #instead of this we use the bellow: res_original.append(left_side[l][0])
                    merge_interval(result2d, left_side[l])
                    l += 1
                else:
                    merge_interval(result2d, right_side[r])
                    r += 1
            while l < len(left_side):
                merge_interval(result2d, left_side[l])
                l += 1
            while r < len(right_side):
                merge_interval(result2d, right_side[r])
                r += 1
            return result2d

        return merge_sort(intervals, 0, len(intervals) - 1)
