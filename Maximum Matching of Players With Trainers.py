class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()

        p = 0
        count = 0

        for trainer in trainers:
            if p < len(players) and players[p] <= trainer:
                count += 1
                p += 1
        return count
