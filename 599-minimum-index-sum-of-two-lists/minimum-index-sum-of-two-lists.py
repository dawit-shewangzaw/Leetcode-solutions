class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        list1_count = len(list1)
        list2_count = len(list2)

        min_sum = 10**9   # large number
        com_str = []

        for i in range(list1_count):
            for j in range(list2_count):

                # If common string found
                if list1[i] == list2[j]:

                    index_sum = i + j

                    # If new minimum found
                    if index_sum < min_sum:
                        min_sum = index_sum
                        com_str = [list1[i]]

                    # If same minimum → add also
                    elif index_sum == min_sum:
                        com_str.append(list1[i])

        return com_str