class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for bank in accounts:
            ans = max(ans,sum(bank))
        return ans    
        