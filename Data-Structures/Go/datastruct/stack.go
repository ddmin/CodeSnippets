package datastruct

import (
	"math"
	"strconv"
	"strings"
)

// stack of ints
type intItem struct {
	val   int
	below *intItem
}

type intStack struct {
	top *intItem
}

// return new instance of stack
func NewIntStack() *intStack {
	return &intStack{nil}
}

// return top of stack
func (s *intStack) Top() (i int, ok bool) {
	if s.IsEmpty() {
		return 0, false
	} else {
		return s.top.val, true
	}
}

// check if stack is empty
func (s *intStack) IsEmpty() bool {
	return s.top == nil
}

// push i on top of stack
func (s *intStack) Push(i int) {
	s.top = &intItem{i, s.top}
}

// pop the top off of stack
func (s *intStack) Pop() {
	if s.IsEmpty() {
		return
	}
	s.top = s.top.below
}

// not struct methods, but related to structs

// testing reversing using stack
func ReverseInteger(n int) int {
	i := 0
	s := NewIntStack()
	for int(math.Pow10(i)) <= n {
		i++
	}
	count := i - 1
	for i > 0 {
		item := n / int(math.Pow10(i-1))
		n -= item * int(math.Pow10(i-1))
		s.Push(item)
		i--
	}
	sum := 0
	for !s.IsEmpty() {
		val, _ := s.Top()
		sum += val * int(math.Pow10(count))
		s.Pop()
		count--
	}
	return sum
}

// stack of strings
type stringItem struct {
	val   string
	below *stringItem
}

type stringStack struct {
	top *stringItem
}

// return new instance of stack
func NewStringStack() *stringStack {
	return &stringStack{nil}
}

// return top of stack
func (s *stringStack) Top() (i string, ok bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		return s.top.val, true
	}
}

// check if stack is empty
func (s *stringStack) IsEmpty() bool {
	return s.top == nil
}

// push i on top of stack
func (s *stringStack) Push(i string) {
	s.top = &stringItem{i, s.top}
}

// pop the top off of stack
func (s *stringStack) Pop() {
	if s.IsEmpty() {
		return
	}
	s.top = s.top.below
}

// string stack implementation of reverse
func ReverseString(i string) string {
	s := NewStringStack()
	result := ""
	for _, i := range i {
		s.Push(string(i))
	}
	for !s.IsEmpty() {
		top, _ := s.Top()
		result += top
		s.Pop()
	}
	return result
}

// convert infix notation to postfix notation
func InfixToPostfix(s string) string {
	result := ""
	stack := NewStringStack()
	for _, c := range strings.Split(s, " ") {
		switch c {
		case "(", "*", "/":
			stack.Push(c)

		case "+", "-":
			t, _ := stack.Top()
			switch t {
			case "*", "/":
				top, _ := stack.Top()
				result += top + " "
				stack.Pop()
				stack.Push(c)
			default:
				stack.Push(c)
			}

		case ")":
			for true {
				top, _ := stack.Top()
				if top == "(" {
					break
				}
				result += top + " "
				stack.Pop()
			}
			stack.Pop()

		default:
			result += c + " "
		}
	}
	for !stack.IsEmpty() {
		top, _ := stack.Top()
		result += top
		if !(stack.top.below == nil) {
			result += " "
		}
		stack.Pop()
	}
	return result
}

// evaluate postfix expression
func EvaluatePostfix(s string) int {
	stack := NewIntStack()
	for _, i := range strings.Split(s, " ") {
		switch i {
		case "+", "-", "*", "/":
			operand2, _ := stack.Top()
			stack.Pop()
			operand1, _ := stack.Top()
			stack.Pop()
			switch i {
			case "+":
				stack.Push(operand1 + operand2)
			case "-":
				stack.Push(operand1 - operand2)
			case "*":
				stack.Push(operand1 * operand2)
			case "/":
				stack.Push(operand1 / operand2)
			}
		default:
			n, _ := strconv.Atoi(string(i))
			stack.Push(n)
		}
	}
	result, _ := stack.Top()
	return result
}

// evaluate infix expression
func EvaluateInfix(s string) int {
	if CheckBracketPairs(s) {
		postfix := InfixToPostfix(s)
		return EvaluatePostfix(postfix)
	} else {
		return 0
	}
}

// stack implementation of bracket pair check
func CheckBracketPairs(exp string) bool {
	s := NewStringStack()
	for _, c := range exp {
		switch string(c) {
		case "(", "{", "[":
			s.Push(string(c))
		case ")":
			if val, _ := s.Top(); val == "(" {
				s.Pop()
			} else {
				return false
			}
		case "}":
			if val, _ := s.Top(); val == "{" {
				s.Pop()
			} else {
				return false
			}
		case "]":
			if val, _ := s.Top(); val == "[" {
				s.Pop()
			} else {
				return false
			}
		}
	}
	_, ok := s.Top()
	if ok {
		return false
	}
	return true
}
