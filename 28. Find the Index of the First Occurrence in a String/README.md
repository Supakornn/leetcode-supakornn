## [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/implement-strstr/)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### 🌟 Example 1:

- **Input:** `haystack = "sadbutsad"`, `needle = "sad"`
- **Output:** `0`
- **Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

### 🌟 Example 2:

- **Input:** `haystack = "leetcode"`, `needle = "leeto"`
- **Output:** `-1`
- **Explanation:** "leeto" did not occur in "leetcode", so we return -1.

### 📋 Constraints:

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## 🎉 Solution:

```golang
func strStr(haystack string, needle string) int {
    if needle == "" {
        return 0
    }
    for i := 0; i < len(haystack)-len(needle)+1; i++ {
        if haystack[i:i+len(needle)] == needle {
            return i
        }
    }
    return -1
}
```
