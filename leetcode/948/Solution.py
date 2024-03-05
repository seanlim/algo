class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        score = 0
        tokens.sort()
        for token in tokens:
            if token > power:
                if score >= 1 and tokens[-1] > token:
                    score-=1
                    power+=tokens.pop()
                else:
                    return score
            power-=token
            score+=1
        return score

