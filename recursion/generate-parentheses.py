# LINK: https://leetcode.com/problems/generate-parentheses/submissions/1234149569/


class Solution:

    @staticmethod
    def adding_brackets(start, end, current_solution_group):
        current_solution_group[start] = "(" + current_solution_group[start]
        current_solution_group[end] = current_solution_group[end] + ")"
        updated_group = []
        for idx, group in enumerate(current_solution_group):
            if idx <= start or idx > end:
                updated_group.append(group)
            else:
                updated_group[-1] = updated_group[-1] + group
        return updated_group

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def choose(i):
            current_solution_group = prev_solutions[-1]
            group_num = len(current_solution_group)

            if i == n:
                result = "".join(current_solution_group.copy())
                if result not in ans:  # củ chuối:
                    ans.append(result)
                return

            for start_candidate in range(0, group_num):
                for end_candidate in range(start_candidate, group_num):
                    candidate_value = self.adding_brackets(
                        start_candidate, end_candidate,
                        current_solution_group.copy())
                    prev_solutions.append(candidate_value)
                    choose(i + 1)
                    prev_solutions.pop(
                    )  # backtrack -> hàm sau đệ quy, 1 trong các bước must have của backtracking

        for group_num in range(1, n + 1):
            current_solution_group = ["()" for _ in range(group_num)]
            prev_solutions = [current_solution_group]  #()()()
            i = group_num
            choose(i)

        return ans
