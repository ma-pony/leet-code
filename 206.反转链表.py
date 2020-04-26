# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    # 当前节点
    curr_node = head
    prev_node = None

    while curr_node is not None:
        # 将当前节点的下一个节点暂存到tmp, 并把上一节点置为当前节点的下一节点
        curr_node.next, temp_node = prev_node, curr_node.next

        # 把tmp节点置为当前节点， 并把当前节点置为上一节点
        prev_node, curr_node = curr_node, temp_node

        # 如果当前节点被置为空则退出循环

    # 返回上一节点
    return prev_node


# 1 -> 2 -> 3

# 1 2 3
def reverse_list2(head: ListNode) -> ListNode:

    if not head or not head.next:
        return head
    p = reverse_list2(head.next)

    head.next.next = head
    head.next = None
    return p


if __name__ == '__main__':
    li1 = ListNode(1)
    li2 = ListNode(2)
    li3 = ListNode(3)
    li1.next = li2
    li2.next = li3
    result = reverse_list2(li1)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)