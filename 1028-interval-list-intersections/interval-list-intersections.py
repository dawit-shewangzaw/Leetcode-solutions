class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        output = []

        if len(firstList) == 0 or len(secondList) == 0:
            return output
        
        while first < len(firstList) and second < len(secondList):
            
            start_max = max(firstList[first][0], secondList[second][0])
            end_min = min(firstList[first][1], secondList[second][1])
            
            if start_max <= end_min:
                output.append([start_max, end_min])
            
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
                
        return output

# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

#         first = 0
#         second = 0
#         output = []
#         firstList.sort()
#         secondList.sort()

#         if len(firstList) == 0 or len(secondList) == 0:
#             return output

#         while first < len(firstList) and second < len(secondList):

#             if firstList[first][0] <= secondList[second][0]:

#                 if firstList[first][1] <= secondList[second][1]:
#                     output += [[secondList[second][0] , firstList[first][1]]]
#                 else:
#                     output += [[secondList[second][0] , secondList[second][1]]]

#             else:
#                 if firstList[first][1] <= secondList[second][1]:
#                     output += [[firstList[first][0] , firstList[first][1]]]
#                 else:
#                     output += [firstList[first][0] , secondList[second][1]]
#                     if [firstList[first][0] , secondList[second][1]]
            
#             first += 1
#             second += 1
#             print("output" + str(output))
        
#         print("output" + str(output))