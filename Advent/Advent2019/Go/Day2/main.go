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

func intcodeComputer(intcode []int) int {
	n := 0
	for intcode[n] != 99 {
		if intcode[n] == 1 {
			sum := intcode[intcode[n+1]] + intcode[intcode[n+2]]
			intcode[intcode[n+3]] = sum
		} else if intcode[n] == 2 {
			prod := intcode[intcode[n+1]] * intcode[intcode[n+2]]
			intcode[intcode[n+3]] = prod
		}
		n += 4
	}
	return intcode[0]
}

func main() {
	dat, err := ioutil.ReadFile("./input")
	check(err)

	data := bytes.Split(dat, []byte(","))

	intcode := make([]int, len(data))
	for n, i := range data {
		intcode[n], err = strconv.Atoi(string(i))
	}

	result := intcodeComputer(intcode)
	fmt.Println("Part 1:", result)

	intcode = make([]int, len(data))
	for n, i := range data {
		intcode[n], err = strconv.Atoi(string(i))
	}

	// could optimize this by making this a function
	// and returning early, so n doesn't run through entire list
	for n := 0; n < 100; n++ {
		for v := 0; v < 100; v++ {
			intcode = make([]int, len(data))
			for n, i := range data {
				intcode[n], err = strconv.Atoi(string(i))
			}
			intcode[1] = n
			intcode[2] = v
			result = intcodeComputer(intcode)
			if result == 19690720 {
				fmt.Println("Part 2", n*100+v)
			}
		}
	}
}
