n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(node, parent, depth):
    depths[node] = depth
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth + 1)

depths = [0] * (n + 1)
dfs(1, -1, 0)

max_depth_node = depths.index(max(depths))

depths = [0] * (n + 1)
dfs(max_depth_node, -1, 0)


tree_diameter = max(depths)
center = depths.index(tree_diameter // 2 + tree_diameter % 2)
print(tree_diameter // 2)


# 트리 센터는 안된다.
# 다른 방법 고민중
