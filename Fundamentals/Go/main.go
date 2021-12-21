package main

import (
	"fmt"
	"strings"

	"github.com/ddmin/fundamentals/datastruct"
)

// to differentiate text
func titleize(s string) {

	length := (80 - len(s) - 2) / 2
	bars := strings.Repeat("=", length)
	fmt.Print("\n", bars, " ", s, " ", bars, "\n\n")
}

// to differentiate different data structures
func separate(s string) {
	length := (78 - len(s) - 2) / 2
	bars := strings.Repeat(" ", length)
	middle := "*" + bars + " " + s + " " + bars + "*"
	cover := strings.Repeat("*", len(middle))

	fmt.Println("\n\n" + cover)
	fmt.Println(middle)
	fmt.Print(cover, "\n\n\n")
}

// test list functionality
func testList() {
	l := datastruct.NewList()
	separate("List")
	l.Display()

	titleize("Prepending")
	for i := 0; i <= 5; i++ {
		l.Prepend(i)
		l.Display()
	}

	titleize("Appending")
	for i := 0; i <= 5; i++ {
		l.Append(i)
		l.Display()
	}

	titleize("Removing")
	for i := 0; i <= 5; i++ {
		l.Remove(i)
		l.Display()
	}

	titleize("Inserting")
	for i := 0; i <= 5; i++ {
		l.Insert(i, 2*i)
		l.Display()
	}

	titleize("Reverse")
	l.Reverse()
	l.Display()

	titleize("Get elements")
	for i := 0; i < 100; i++ {
		val, ok := l.Get(i)
		if ok {
			fmt.Print(val, " ")
		}
	}
	fmt.Println()
}

// test linked list functionality
func testLinkedList() {
	l := datastruct.NewLinkedList()
	separate("Linked List")
	l.Display()

	titleize("Prepending")
	for i := 0; i <= 8; i++ {
		l.Prepend(i)
		l.Display()
	}

	titleize("Appending")
	for i := 1; i <= 4; i++ {
		l.Append(i)
		l.Display()
	}

	titleize("Inserting")
	for i := 2; i <= 8; i += 2 {
		l.Insert(i, i)
		l.Display()
	}

	titleize("Remove First")
	for i := 0; i < 3; i++ {
		l.RemoveFirst()
		l.Display()
	}

	titleize("Remove Last")
	for i := 0; i < 3; i++ {
		l.RemoveLast()
		l.Display()
	}

	titleize("Remove")
	for i := 0; i < 3; i++ {
		l.Remove(1)
		l.Display()
	}

	titleize("Reverse")
	a := datastruct.NewLinkedList()
	for n := 0; n < 10; n++ {
		a.Display()
		a.Reverse()
		a.Display()
		a.Append(n)
	}

	l.Reverse()
	l.Display()

	titleize("Get elements")
	for i := 0; i < 100; i++ {
		val, ok := l.Get(i)
		if ok {
			fmt.Print(val, " ")
		}
	}
	fmt.Println()

	titleize("Recursive")
	l.RecurseReverse()
	l.Display()

	titleize("Display reversed")
	l.DisplayReversed()
}

// test doubly linked list functionality
func testDoublyLinked() {
	d := datastruct.NewDoublyLinked()
	separate("Doubly Linked")
	d.Display()

	titleize("Prepending")
	for i := 0; i < 3; i++ {
		d.Prepend(-i)
		d.Display()
	}

	titleize("Appending")
	for i := 0; i < 3; i++ {
		d.Append(-i)
		d.Display()
	}

	titleize("Inserting")
	for i := 0; i < 10; i++ {
		d.Insert(2*i, i)
		d.Display()
	}

	titleize("Remove First")
	for i := 0; i < 4; i++ {
		d.RemoveFirst()
		d.Display()
	}

	titleize("Remove Last")
	for i := 0; i < 7; i++ {
		d.RemoveLast()
		d.Display()
	}

	titleize("Remove")
	d.Remove(0)
	d.Remove(4)
	d.Display()

	titleize("Reverse")
	a := datastruct.NewDoublyLinked()
	for n := 0; n < 10; n++ {
		a.Display()
		a.Reverse()
		a.Display()
		a.Append(n)
	}
}

// test int stack functionality
func testIntStack() {
	s := datastruct.NewIntStack()
	separate("Int Stack")
	titleize("Pushing")
	for i := 0; i <= 10; i++ {
		s.Push(i)
		n, ok := s.Top()
		if ok {
			fmt.Println("Top:", n)
		}
	}
	titleize("Popping")
	for i := 0; i < 12; i++ {
		s.Pop()
		n, ok := s.Top()
		if ok {
			fmt.Println("Top:", n)
		} else {
			fmt.Println("Stack is empty!")
		}
	}
	titleize("Reversing integer (using stacks)")
	for _, integer := range [...]int{1000, 12419, 28072, 5, 19, 10012} {
		fmt.Println(integer, "->", datastruct.ReverseInteger(integer))
	}
	titleize("Check for matching braces")

	strings := [...]string{
		"func return5() {int x:=5; return x}",
		"(())))",
		"((((((((())))))))",
		"{[something((interesting[]))]}0",
	}

	for _, i := range strings {
		fmt.Println(i, "->", datastruct.CheckBracketPairs(i))
	}
}

// test int stack functionality
func testStringStack() {
	s := datastruct.NewStringStack()
	separate("String Stack")
	titleize("Pushing")
	for _, i := range [...]string{
		"Zero",
		"One",
		"Two",
		"Three",
		"Four",
		"Five",
		"Six",
		"Seven",
		"Eight",
		"Nine",
		"Ten",
	} {
		s.Push(i)
		n, ok := s.Top()
		if ok {
			fmt.Println("Top:", n)
		}
	}

	titleize("Popping")
	for i := 0; i < 12; i++ {
		s.Pop()
		n, ok := s.Top()
		if ok {
			fmt.Println("Top:", n)
		} else {
			fmt.Println("Stack is empty!")
		}
	}

	titleize("Reversing strings (using stacks)")
	for _, str := range [...]string{
		"Hello World!",
		"This will be reversed",
		"A Toyota Racecar",
	} {
		fmt.Println(str, "->", datastruct.ReverseString(str))
	}

	titleize("Infix -> Postfix")
	equations := []string{
		"( 7 / ( 3 + 4 ) ) * 9 * ( 8 - 4 )",
		"3 * ( 6 + 2 )",
		"( ( 5 + 2 ) * 5 - 1 ) * 3",
		"9 * ( 4 + 5 ) )",
	}

	postfix := []string{}

	for _, eq := range equations {
		if datastruct.CheckBracketPairs(eq) {
			converted := datastruct.InfixToPostfix(eq)
			fmt.Println(eq, " -> ", converted)
			postfix = append(postfix, converted)
		} else {
			fmt.Println("Syntax Error: ", eq)
		}
	}

	titleize("Evaluate Postfix")
	for _, eq := range postfix {
		fmt.Println("("+eq+") -> ", datastruct.EvaluatePostfix(eq))
	}

	titleize("Evaluate Infix")
	equation := "( 72 / 3 ) / ( 1 + ( 75 / 25 ) )"
	bad_equation := "( 72 / 3 ) / ( 1 + ( 75 / 25 )"
	fmt.Println(equation, "->", datastruct.EvaluateInfix(equation))
	fmt.Println(bad_equation, "  ->", datastruct.EvaluateInfix(bad_equation))
}

func main() {
	// list-like data structures
	testList()
	testLinkedList()
	testDoublyLinked()

	// test stack data structures
	testIntStack()
	testStringStack()
}
