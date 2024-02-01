package main

import (
	"log"
	"reflect"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	var result []int
	var i, j int
	for i+j < m+n {
		if j == n || nums1[i] <= nums2[j] && i < m {
			result = append(result, nums1[i])
			i++
		} else {
			result = append(result, nums2[j])
			j++
		}
	}
	copy(nums1, result)
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3

	merge(nums1, m, nums2, n)

	expeted := []int{1, 2, 2, 3, 5, 6}

	if !reflect.DeepEqual(nums1, expeted) {
		log.Fatalf("Los slices no son iguales %v!=%v", nums1, expeted)
	}

	nums1 = []int{1}
	m = 1
	nums2 = []int{}
	n = 0

	merge(nums1, m, nums2, n)

	expeted = []int{1}

	if !reflect.DeepEqual(nums1, expeted) {
		log.Fatalf("Los slices no son iguales %v!=%v", nums1, expeted)
	}

	nums1 = []int{0}
	m = 0
	nums2 = []int{1}
	n = 1

	merge(nums1, m, nums2, n)

	expeted = []int{1}

	if !reflect.DeepEqual(nums1, expeted) {
		log.Fatalf("Los slices no son iguales %v!=%v", nums1, expeted)
	}

}
