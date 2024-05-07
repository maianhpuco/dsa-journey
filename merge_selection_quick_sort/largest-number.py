#: link: https://leetcode.com/problems/largest-number/


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        '''
        nums -> form the largest number 
        [10, 2] -> "210" 
        [3,30,34,5,9] -> [9 5 34 3 30] #f compare: a and b (from left to right)
        find the "largest" in an array/subarray binary/O(n)

        [1113,111311] 
        1113_1113_11 yes 
        111311_1113 
        [432,43243]
        432_432|43
                 k = 0-> len(a_head)
                if k > len(a): 
                    i =  k - len(k) 
                    target_array  = array(b)
                -> return the value of slicing 
        a_head = 432|43243 
                      ^i
        b_head = 43243|432   
                       ^j  

        a = 432  
            j  i       
        b = 432 43
             i   j 
        a_head = 432 43i243 
        b_head = 43243j 432 yes  

        - note: edge case 0 0 
        - there are 2 steps: (1) compare (2) form a number ex: 0, 1 -> 1 

    
        '''

        def value_at_current_position(head: str, tail: str, index: int) -> str:
            '''
            return the current value if the target array was formed by [head, tail] 
        
            '''
            if index < len(head):
                return head[index]
            else:
                return tail[index - len(head)]

        def is_larger(a: int, b: int):  #3 and 34
            '''
            compare O(n)
            edge case: 0 0 
            '''
            str_a, str_b = str(a), str(b)
            for k in range(len(str_a) + len(str_b)):
                i_str = value_at_current_position(str_a, str_b, k)
                j_str = value_at_current_position(str_b, str_a, k)
                if i_str > j_str:
                    return True
                elif i_str < j_str:
                    return False
            return True

        def merge_sort_string(array, left, right):
            '''
            find the "largest" element in the array, "largest" was define by the compare function 
            using merge_sort [3,30,34,5,9] O(nlogn) 
            '''
            mid = left + (right - left) // 2
            #basecase
            if left == right:
                return array[left:right + 1]
            left_side = merge_sort_string(array, left, mid)
            right_side = merge_sort_string(array, mid + 1, right)

            l, r = 0, 0
            res = []
            while l < len(left_side) and r < len(right_side):
                if is_larger(left_side[l], right_side[r]):  #left[l] < right[r]
                    res.append(left_side[l])
                    l += 1
                else:
                    res.append(right_side[r])
                    r += 1

            while l < len(left_side):
                res.append(left_side[l])
                l += 1
            while r < len(right_side):
                res.append(right_side[r])
                r += 1
            return res

        array_result = merge_sort_string(nums, 0, len(nums) - 1)
        str_result = ''
        curr_index = 0
        for value in array_result:
            if curr_index == 0 and value == 0:
                pass
            else:
                curr_index += 1
                str_result += str(value)
        if str_result == '' and nums != []:
            str_result = '0'
        #return "".join([str(i) for i in array_result])
        return str_result
