class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] 

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)

        return result