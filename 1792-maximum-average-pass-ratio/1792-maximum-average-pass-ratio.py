import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the improvement in pass ratio if one extra student is added
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total

        # Max heap to prioritize classes with the highest improvement
        max_heap = [(-(improvement(p, t)), p, t) for p, t in classes]
        heapq.heapify(max_heap)

        # Assign extra students
        for _ in range(extraStudents):
            imp, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-(improvement(p, t)), p, t))

        # Calculate the final average pass ratio
        return sum(p / t for _, p, t in max_heap) / len(classes)
