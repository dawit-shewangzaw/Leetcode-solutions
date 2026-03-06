class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        max_match = 0
        player = 0
        trainer = 0
        
        while len(trainers) != 0 and len(players) != 0: 
            if players[player] <= trainers[trainer]:
                players.remove(players[player])
                trainers.remove(trainers[trainer])
                max_match += 1
            else:
                trainers.remove(trainers[trainer])
        return max_match