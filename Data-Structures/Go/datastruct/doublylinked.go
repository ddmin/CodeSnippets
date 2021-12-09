package datastruct

import (
	"fmt"
	"strconv"
)

type doubleNode struct {
	val  int
	prev *doubleNode
	next *doubleNode
}

type doublylinked struct {
	head *doubleNode
	size int
}

// return a new instance of a doubly linked list
func NewDoublyLinked() *doublylinked {
	return &doublylinked{nil, 0}
}

// display doubly linked
func (d *doublylinked) Display() {
	// empty list
	if d.head == nil {
		fmt.Println("[ ]")
		return
	}

	str := "[ "
	temp := d.head
	str += strconv.Itoa(temp.val) + " "

	// traverse list until end
	for temp.next != nil {
		temp = temp.next
		str += strconv.Itoa(temp.val) + " "
	}

	str += "]"
	fmt.Println(str)
}

// get ith item of list
func (d *doublylinked) Get(i int) (n int, ok bool) {
	if i < d.size {
		temp := d.head
		for count := 0; count < i; count++ {
			temp = temp.next
		}
		return temp.val, true
	} else {
		return 0, false
	}
}

// insert i as first element in list
func (d *doublylinked) Prepend(i int) {
	// if empty list
	if d.head == nil {
		d.head = &doubleNode{i, nil, nil}
		d.size = 1
	}
	// save original head to temp
	temp := d.head
	// set head to new node
	d.head = &doubleNode{i, nil, temp}
	temp.prev = d.head
	d.size++
}

// insert i at end of list
func (d *doublylinked) Append(i int) {
	// if list is empty,
	if d.head == nil {
		d.head = &doubleNode{i, nil, nil}
		d.size = 1
		return
	}

	temp := d.head
	for temp.next != nil {
		temp = temp.next
	}
	temp.next = &doubleNode{i, temp, nil}
	d.size++
}

// insert i at position n
func (d *doublylinked) Insert(i, n int) {
	if n == 0 {
		d.Prepend(i)
	} else if n == d.size {
		d.Append(i)
	} else if n < d.size {
		count := 0
		temp := d.head
		for count < n {
			temp = temp.next
			count++
		}
		insertion := &doubleNode{i, temp.prev, temp}
		temp.prev.next = insertion
		temp.prev = insertion
		d.size++
	} else {
		return
	}
}

// remove head node
func (d *doublylinked) RemoveFirst() {
	if d.size == 1 {
		d.head = nil
		d.size--
		return
	}

	d.head = d.head.next
	d.head.prev = nil
	d.size--
}

// remove tail node
func (d *doublylinked) RemoveLast() {
	temp := d.head
	for temp.next != nil {
		temp = temp.next
	}
	temp.prev.next = nil
	d.size--
}

// remove node at position n
func (d *doublylinked) Remove(n int) {
	if n == 0 {
		d.RemoveFirst()
	} else if d.size-1 == n {
		d.RemoveLast()
	} else if d.size > n {
		count := 0
		temp := d.head
		for count < n {
			temp = temp.next
			count++
		}
		prev := temp.prev
		temp.prev.next = temp.next
		temp.next.prev = prev
		d.size--
	} else {
		return
	}
}

// reverse elements in list
func (d *doublylinked) Reverse() {
	temp := d.head
	for temp != nil {
		next := temp.next
		temp.next = temp.prev
		temp.prev = next
		d.head = temp
		temp = temp.prev
	}
}
