class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        prev = None
        cost = 0

        time_acc = -1
        time_acc_max = 0

        for i, c in enumerate(colors):
            if prev == c:
                if time_acc == -1:
                    # if the accumulator is empty when we spot a new common subsequence,
                    # initialise it with the cost of the prev balloon
                    prev_cost = neededTime[i-1]
                    time_acc = prev_cost
                    time_acc_max = prev_cost
                current_cost = neededTime[i]
                time_acc += current_cost
                time_acc_max = max(time_acc_max, current_cost)
            elif time_acc != -1:
                # non-matching sequence with nonempty accumulator,
                # this implies that we have reached the end of a sequence
                # to resolve a sequence, simply minus the max value from sum
                cost += time_acc - time_acc_max
                # reset accumulator
                time_acc = -1
                time_acc_max = 0

            # update the previous color before looping
            prev = c

        # last check in case there is a sequence at the end
        if time_acc != -1:
            cost += time_acc - time_acc_max

        return cost
