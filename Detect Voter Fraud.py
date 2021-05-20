class Solution:
    def solve(self, votes):
        voters = set()
        for vote in votes:
            if vote[1] in voters:
                return True
            voters.add(vote[1])
        return False
