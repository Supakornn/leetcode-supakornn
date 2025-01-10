package main

import "fmt"

func romanToInt(s string) int {
	roman := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	result := 0

	for i := range s {
		if i < len(s)-1 && roman[string(s[i])] < roman[string(s[i+1])] {
			result -= roman[string(s[i])]
		} else {
			result += roman[string(s[i])]
		}
	}
	return result

}

func main() {
	fmt.Println(romanToInt("III")) // 3
}
