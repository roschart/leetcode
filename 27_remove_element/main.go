package main

import "fmt"

func removeElement(nums []int, val int) int {
	i, k, result := 0, len(nums)-1, 0
	for i < k {
		if nums[i] == val {
			n := nums[k]
			nums[k] = nums[i]
			nums[i] = n
			k--
			result++
			continue
		}
		i++
	}
	return len(nums) - result
}

func main() {
	nums := []int{1}
	x := removeElement(nums, 1)
	fmt.Println(x, nums)
}
