alphabet = list('abcdefghijklmnopqrstuvwxys')

# BFS with a queue
# def word_ladder(start, end, word_list):
#     word_list = set(word_list)
#     if end not in word_list:
#         return 0
#     seen = {start: 1}
#     q = [start]
#
#     while q:
#         w = q.pop(0)
#         num_moves = seen[w]
#
#         for i, _ in enumerate(w):
#             w2 = list(w)
#             for ch in alphabet:
#                 w2[i] = ch
#                 new_w = ''.join(w2)
#                 if new_w not in word_list:
#                     continue
#                 if new_w == end:
#                     return num_moves + 1
#                 if new_w not in seen:
#                     seen[new_w] = num_moves + 1
#                     q.append(new_w)
#     return 0

# Two sided approach.
def word_ladder(start, end, word_list):
    def replace_letter(word, idx, letter):
        return word[:idx] + letter + word[idx + 1:]

    word_list = set(word_list)
    if end not in word_list:
        return 0

    start_set = {start}
    end_set = {end}
    seen = set()

    num_steps = 2
    while start_set:
        if len(start_set) > len(end_set):
            start_set, end_set = end_set, start_set

        new_set = set()
        for word in start_set:
            for i in range(len(word)):
                for c in alphabet:
                    new_word = replace_letter(word, i, c)
                    if new_word in end_set:
                        return num_steps
                    if new_word not in seen and new_word in word_list:
                        seen.add(new_word)
                        new_set.add(new_word)
        num_steps += 1
        start_set = new_set
        print start_set, num_steps
    return 0


t1 = word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print t1
