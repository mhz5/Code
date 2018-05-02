def lowest_common_ancestor(root, p, q):
    parent = {root: None}

    stack = [root]
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(parent[p])
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q


def lowest_common_ancestor2(root, p, q):
    if root is None or root == p or root == q:
        return root

    left_lca = lowest_common_ancestor2(root.left, p, q)
    right_lca = lowest_common_ancestor2(root.right, p, q)

    if left_lca:
        return left_lca
    if right_lca:
        return right_lca
    return root




