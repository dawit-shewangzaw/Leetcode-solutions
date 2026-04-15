class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)        
        answer = [0] * temp_len
        stack = []
        
        for i , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         temp_len = len(temperatures)

#         answer = [0] * temp_len
#         left , right = 0 , 1

#         if temp_len == 1:
#             return answer

#         for i in range(temp_len):
#             count = 1
#             while right < temp_len:
#                 if temperatures[left] < temperatures[right]:
#                     answer[i] = count
#                     break
#                 else:
#                     count += 1
#                 right += 1
#             left += 1
#             right = left + 1 
        
#         return answer