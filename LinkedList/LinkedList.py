class Node:
    def __init__(self,prev,elent,next):
        self.val = elent
        self.next = next
        self.prev = prev

#创建链表
class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def createLinkedList(arr: 'list[int]') -> 'LinkedNode':
    if arr is None or len(arr) == 0:
        return None
    head = LinkedNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        cur.next = LinkedNode(arr[i])
        cur = cur.next
    return head

#查
head = createLinkedList([1,2,3,4,5])
def find(head) :
    p = head
    while p:
        print(p.val)
        p = p.next

#增
head = createLinkedList([1,2,3,4,5])
#头部插入
def insert(head,val) :
    new_node = LinkedNode(val)
    new_node.next = head
    return new_node
#尾部插入
def append(head,val) :
    p = head
    while p.next:
        p = p.next
    p.next = LinkedNode(val)
    return head

#中间插入
def insert_after(head,val,x) :
    p = head
    for _ in range(x-1):
        p = p.next
    new_node = LinkedNode(val)
    new_node.next = p.next
    p.next = new_node
    return head
# find(insert_after(head,6,3))
#删
def delete(head,val) :
    if head.val == val:
        return head.next
    p = head
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
            return head
        p = p.next
    return head

# find(delete(head,3))