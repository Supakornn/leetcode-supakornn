package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	max := 0

	for i, v := range s {
		m := make(map[rune]bool)
		m[v] = true
		count := 1

		for _, w := range s[i+1:] {
			if _, ok := m[w]; ok {
				break
			}

			m[w] = true
			count++
		}

		if count > max {
			max = count
		}
	}

	return max
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb")) // 3
}
