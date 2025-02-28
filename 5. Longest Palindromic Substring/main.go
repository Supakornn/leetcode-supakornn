package main

import (
	"fmt"
)

func longestPalindrome(s string) string {
	lenght := len(s)

	if lenght <= 1 {
		return s
	}

	start, end := 0, 0

	for i := range s {
		len1, len2 := getPalindrom(s, i, i), getPalindrom(s, i, i+1)
		maxLen := max(len1, len2)

		if maxLen > end-start {
			start = i - (maxLen-1)/2
			end = i + maxLen/2
		}
	}

	return s[start : end+1]
}

func getPalindrom(s string, left, right int) int {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left, right = left-1, right+1
	}

	return right - left - 1
}

func main() {
	fmt.Println(longestPalindrome("babad")) // bab
	fmt.Println(longestPalindrome("ccc"))   // bab
}
