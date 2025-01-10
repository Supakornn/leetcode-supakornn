package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	words := strings.Fields(s)
	return len(words[len(words)-1])
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World")) // 5
}
