class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAl=0
        maxAlt=currAl
        for i in range(len(gain)):
            currAl += gain[i]
            maxAlt = max(currAl,maxAlt)
        return maxAlt
