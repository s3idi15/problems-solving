class Solution:
    def minRecorder(self, n: int, connections: list[list[int]]) -> int:
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges

        # Time: O(n)
        # Memory: O(n)

        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visit = set()
        change = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)