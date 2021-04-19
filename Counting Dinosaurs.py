from collections import Counter


class Solution:
    def solve(self, animals, dinosaurs):
        return sum([count for animal, count in Counter(animals).items() if animal in dinosaurs])