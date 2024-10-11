import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        # Pairing arrival time with index of each friend, since we need to track the targetFriend
        events = []
        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, i, 'arrive'))
            events.append((leave, i, 'leave'))

        # Sort events based on time; for tie-breakers, 'leave' should come before 'arrive'
        events.sort(key=lambda x: (x[0], x[2] == 'arrive'))

        # To track available chairs
        available_chairs = []
        # The map of friends to the chair they sit in
        friend_chair_map = {}
        current_chair = 0
        
        # Process each event
        for time, friend, action in events:
            if action == 'arrive':
                # If there are free chairs, take the smallest one
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = current_chair
                    current_chair += 1

                friend_chair_map[friend] = chair

                # If it's the target friend, return the chair
                if friend == targetFriend:
                    return chair

            elif action == 'leave':
                # When a friend leaves, their chair becomes available
                heapq.heappush(available_chairs, friend_chair_map[friend])

        return -1
