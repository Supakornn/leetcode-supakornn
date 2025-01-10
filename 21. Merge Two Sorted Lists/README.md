## [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

- You are given the heads of two sorted linked lists `list1` and `list2`.

- Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

- Return the head of the merged linked list.

![Merge Example](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

### 🌟 Example 1:

- **Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`
- **Output:** `[1,1,2,3,4,4]`

### 🌟 Example 2:

- **Input:** `list1 = []`, `list2 = []`
- **Output:** `[]`

### 🌟 Example 3:

- **Input:** `list1 = []`, `list2 = [0]`
- **Output:** `[0]`

### 📋 Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## 🎉 Solution:

```golang
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}

	if list2 == nil {
		return list1
	}

	if list1.Val < list2.Val {
		list1.Next = mergeTwoLists(list1.Next, list2)
		return list1
	} else {
		list2.Next = mergeTwoLists(list1, list2.Next)
		return list2
	}
}
```
