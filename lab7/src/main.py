import csv


class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


def calculate_minimum_cable(filepath: str):
    edges = []
    vertices = set()

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    u = row[0].strip()
                    v = row[1].strip()
                    weight = float(row[2].strip())
                    edges.append((weight, u, v))
                    vertices.add(u)
                    vertices.add(v)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {filepath} не знайдено.")

    if not vertices:
        return 0, 0

    n = len(vertices)
    edges.sort()
    dsu = DSU(vertices)

    mst_weight = 0.0
    edges_added = 0
    max_single_cable = 0.0

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst_weight += weight
            edges_added += 1

            max_single_cable = weight

            if edges_added == n - 1:
                break

    if edges_added < n - 1:
        return -1

    return int(mst_weight), int(max_single_cable)
