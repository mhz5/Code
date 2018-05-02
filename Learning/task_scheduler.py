from operator import itemgetter


def task_scheduler(tasks, n):
    task_dict = {}

    for t in tasks:
        if t not in task_dict:
            task_dict[t] = 1
        else:
            task_dict[t] += 1

    grouped_tasks = [(task, task_dict[task]) for task in task_dict]
    sorted_tasks = sorted(grouped_tasks, key=itemgetter(1), reverse=True)

    max_tasks = sorted_tasks[0][1]
    num_max = 0
    for t, count in sorted_tasks:
        if count == max_tasks:
            num_max += 1
        else:
            break

    min_cycles = (max_tasks - 1) * (n + 1) + num_max
    x = sum([t[1] for t in sorted_tasks])
    return max(x, min_cycles)

t1 = task_scheduler(["A","A","A","B","B","B"], 2)
print t1
