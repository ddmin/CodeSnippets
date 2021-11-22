package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := ioutil.ReadFile("./input")
	check(err)

	sum1 := 0
	data := bytes.Split(dat, []byte("\n"))
	data = data[:len(data)-1]

	for _, n := range data {
		i, err := strconv.Atoi(string(n))
		check(err)
		sum1 += (i / 3) - 2
	}
	// answer to part 1
	fmt.Println("Part 1:", sum1)

	sum2 := 0
	for _, n := range data {
		i, err := strconv.Atoi(string(n))
		check(err)
		for i > 0 {
			temp := (i / 3) - 2
			i = temp
			if temp > 0 {
				sum2 += temp
			}
		}
	}
	// answer to part 2
	fmt.Println("Part 2:", sum2)
}
