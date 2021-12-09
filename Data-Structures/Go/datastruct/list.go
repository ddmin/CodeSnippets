package datastruct

import (
	"fmt"
	"strconv"
)

type list struct {
	// maximum capacity of array
	max int
	// end of current list (number of items in list)
	size int
	// array slice representing items in list
	arr []int
}

// create new list instance
func NewList() *list {
	return &list{2, 0, make([]int, 2)}
}

// display list
func (l *list) Display() {
	str := "["
	for i := 0; i < l.size; i++ {
		str += strconv.Itoa(l.arr[i])
		if i != l.size-1 {
			str += " "
		}
	}
	str += "]"
	fmt.Println(str)
}

// get element i from list
func (l *list) Get(i int) (n int, ok bool) {
	if i < l.size {
		return l.arr[i], true
	} else {
		return 0, false
	}
}

// adjust max size of list
// copy list into longer array slice
func (l *list) adjustLength() {
	if l.max <= l.size {
		// create array slice with double capacity
		l.max *= 2
		temp := make([]int, l.max)
		// copy elements
		for c := 0; c < l.size; c++ {
			temp[c] = l.arr[c]
		}
		// point to new array slice
		l.arr = temp
	}
}

// insert i at end of list
func (l *list) Append(i int) {
	// check for room
	l.adjustLength()
	// add to end of array slice
	l.arr[l.size] = i
	// increment size of array by 1
	l.size += 1
}

// insert i at beginning of list
func (l *list) Prepend(i int) {
	l.Insert(i, 0)
}

// insert i at position n
func (l *list) Insert(i, n int) {
	// check for room
	l.adjustLength()
	// shift every element >= n up 1
	for c := l.size - 1; c >= n; c-- {
		l.arr[c+1] = l.arr[c]
	}
	// insert item
	l.arr[n] = i
	// increment size of array by 1
	l.size += 1
}

// remove element at position n
func (l *list) Remove(n int) {
	// shift every element > n down 1
	for c := n + 1; c < l.size; c++ {
		l.arr[c-1] = l.arr[c]
	}
	// decrement size of array by 1
	l.size -= 1
}

// reverse elements in list
func (l *list) Reverse() {
	if l.size == 0 || l.size == 1 {
		return
	}
	temp := make([]int, l.size)
	for i := 0; i < l.size; i++ {
		temp[i], _ = l.Get(l.size - 1 - i)
	}
	l.arr = temp
}
