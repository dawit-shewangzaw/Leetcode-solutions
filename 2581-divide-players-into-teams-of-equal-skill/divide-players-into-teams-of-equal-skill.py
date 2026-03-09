class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        left = 0
        right = len(skill) - 1
        total = 0

        first_team_skill = skill[left] + skill[right]

        while left <= right:
            teams_skill  = skill[left] + skill[right]
            
            if first_team_skill != teams_skill:
                return -1
            else:
                total += skill[left] * skill[right]
                left += 1
                right -= 1
    
        return total    