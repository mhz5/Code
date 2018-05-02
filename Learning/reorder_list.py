class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reorder_list(head):
    """
    :type head: ListNode
    """
    i = 0
    mid = cur = head
    while cur is not None:
        cur = cur.next
        i += 1
        if i % 2 == 0:
            mid = mid.next

    last_half = mid.next
    mid.next = None
    # reversed
    end = reverse_list(last_half)
    print(list_to_str(end))

    cur = head
    while cur and end:
        next_cur = cur.next
        next_end = end.next
        cur.next = end
        end.next = next_cur
        cur = next_cur
        end = next_end
    return head


def reverse_list(r):
    cur = r
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev, cur = cur, next

    return prev


def make_list(vals):
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next

    return head


def list_to_str(head):
    vals = []
    while head is not None:
        vals.append(head.val)
        head = head.next

    return ", ".join([str(v) for v in vals])


vals = [1,2,3,4,5,6,7,8]
l = make_list(vals)
rol = reorder_list(l)
print rol
print list_to_str(rol)


print "Done"


