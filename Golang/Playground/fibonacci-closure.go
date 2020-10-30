package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	curr := 0
	prevList := []int{0, 0, 1}

	return func() int {
		prevList = append(prevList, prevList[curr+1]+prevList[curr+2])
		curr++
		return prevList[curr]
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 93; i++ {
		fmt.Println(f())
	}
}
