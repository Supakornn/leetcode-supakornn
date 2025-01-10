## [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### 🌟 Example 1:

- **Input:** `s = "()"`
- **Output:** `true`

### 🌟 Example 2:

- **Input:** `s = "()[]{}"`
- **Output:** `true`

### 🌟 Example 3:

- **Input:** `s = "(]"`
- **Output:** `false`

### 🌟 Example 4:

- **Input:** `s = "([])"`
- **Output:** `true`

### 📋 Constraints:

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only '()[]{}'.

## 🎉 Solution:

```golang
func isValid(s string) bool {
    m := map[byte]byte{
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack := make([]byte, 0)
    for i := 0; i < len(s); i++ {
        if len(stack) > 0 && stack[len(stack)-1] == m[s[i]] {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, s[i])
        }
    }
    return len(stack) == 0
}
```
