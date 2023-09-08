# https://leetcode.com/problems/merge-sorted-array/
# array: pop, append


class Solution:
    def merge(self, num1: list[int], num2: list[int], m: int, n: int) -> int:
        """
        result:
            [1, 2, 3, 3, 5, 6]

        n1 = ^[1, 2, 4, 0,, 0, 0]
        n2 = ^[2, 3, 5]

        n1 =  [1, 3, 3^, 0, 0, 0]
        n2 =  [2^, 3, 5]

        n1 = [1, 2, ]
        compare 2 pointer:
        if p1<(m-1):
            if  p1 <= p2:
                p1+=1,
            else:
                swap n1[p1] vs n1[p2]
                then resorting for p2 by comparing the next position
        else:
            n1.append()

        """

        p = 0
        q = 0
        # specical situation : p, q does not exist m=0 | n=0
        if n == 0:
            return num1

        while p < m and m > 0:
            if num1[p] <= num2[q]:
                p += 1  # n1 move right of correct
            else:  # else swap and move the n1[p] to correct position on
                temp = num1[p]
                num1[p] = num2[q]
                num2[q] = temp

                # resorting the num2 by : find correct position
                # for value at [q] by resorting the array
                curr = q
                while curr < (n - 1) and num2[curr] > num2[curr + 1]:
                    print("true")
                    t = num2[curr]
                    num2[curr] = num2[curr + 1]
                    num2[curr + 1] = t
                    curr += 1
            print(p, num1, num2)
        while p < (m + n):
            num1[p] = num2[q]
            p += 1
            q += 1
            print(p, num1, num2)

        return num1


if __name__ == "__main__":
    num_1 = [1, 2, 4, 0, 0, 0]
    num_2 = [2, 3, 6]
    num_1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    num_2 = [1, 2, 2]

    num_1 = [-1, 0, 0, 1, 3, 3, 0, 0, 0]
    num_2 = [3, 2, 2]

    m = 6
    n = 3
    solution = Solution()
    result = solution.merge(num_1, num_2, m, n)
    print(result)
