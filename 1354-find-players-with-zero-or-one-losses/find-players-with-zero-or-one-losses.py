class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] = losses.get(loser, 0) + 1

        zero_loss = []
        one_loss = []

        for player in players:
            if player not in losses:
                zero_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]
