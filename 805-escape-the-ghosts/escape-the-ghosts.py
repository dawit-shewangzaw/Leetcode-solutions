class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        your_dist = abs(target[0]) + abs(target[1])
        for g in ghosts:
            ghost_dist = abs(g[0] - target[0]) + abs(g[1] - target[1])
            if ghost_dist <= your_dist:
                return False

        return True
