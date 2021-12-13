class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(list(filter(lambda a: a in jewels, list(stones))))