class Solution:
    def findRelativeRanks(self, score):
        # Sort the scores in descending order and keep track of the original indices
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        
        # Create an array for the results
        result = [""] * len(score)
        
        # Assign ranks based on the sorted order
        for i, (idx, _) in enumerate(sorted_scores):
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i + 1)
        
        return result
