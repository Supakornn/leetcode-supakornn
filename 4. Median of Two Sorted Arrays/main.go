package main

import "fmt"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	for i := 0; i < len(nums2); i++ {
		nums1 = append(nums1, nums2[i])
	}

	for i := 0; i < len(nums1); i++ {
		for j := i + 1; j < len(nums1); j++ {
			if nums1[i] > nums1[j] {
				nums1[i], nums1[j] = nums1[j], nums1[i]
			}
		}
	}

	if len(nums1)%2 == 0 {
		return float64(nums1[len(nums1)/2]+nums1[len(nums1)/2-1]) / 2
	}

	return float64(nums1[len(nums1)/2])
}

func main() {
	fmt.Println(findMedianSortedArrays([]int{1, 2}, []int{3, 4})) // 2.5
}
