package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func rot13(b byte) byte {
	switch {
	case b > 64 && b < 91:
		return ((b-65)+13)%26 + 65
	case b > 97 && b < 123:
		return ((b-97)+13)%26 + 97
	default:
		return b
	}
}

func (r13 rot13Reader) Read(b []byte) (int, error) {
	val, err := r13.r.Read(b)
	for i := 0; i < val; i++ {
		b[i] = rot13(b[i])
	}
	return val, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!\n")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
