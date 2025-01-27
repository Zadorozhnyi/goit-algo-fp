class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted_lists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.value < l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

    def sort(self):
        if not self.head or not self.head.next:
            return self.head
        self.head = self.merge_sort(self.head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        return self.merge_sorted_lists(left, right)

    def get_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Тестування однозв'язного списку
ll = LinkedList()
for num in [4, 2, 1, 3]:
    ll.append(num)

print("Оригінальний список:")
ll.display()

ll.reverse()
print("Реверсований список:")
ll.display()

ll.sort()
print("Відсортований список:")
ll.display()

# Тестування злиття двох відсортованих списків
l1 = LinkedList()
l2 = LinkedList()
for num in [1, 3, 5]:
    l1.append(num)
for num in [2, 4, 6]:
    l2.append(num)

merged_head = ll.merge_sorted_lists(l1.head, l2.head)
merged_list = LinkedList()
merged_list.head = merged_head
print("Об'єднаний відсортований список:")
merged_list.display()
