from copy import copy

NOT_SEEN = -1
SEEN_TMP = 0
SEEN_PERM = 1

def can_finish(num_courses, prereqs):
    deps = {i: set() for i in range(num_courses)}

    for [course, req] in prereqs:
        deps[course].add(req)

    seen = [NOT_SEEN for _ in range(num_courses)]
    for course in deps:
        if not dfs(deps, seen, course):
            return False

    return True


def dfs(deps, seen, course):
    if seen[course] == SEEN_PERM:
        return True
    if seen[course] == SEEN_TMP:
        return False
    seen[course] = SEEN_TMP

    for dep in deps[course]:
        if not dfs(deps, seen, dep):
            return False

    seen[course] = SEEN_PERM
    return True

