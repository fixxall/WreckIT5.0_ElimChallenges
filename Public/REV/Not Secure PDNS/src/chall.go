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

// ReverseBytes reverses the byte slice.
func ReverseBytes(data []byte) []byte {
	for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
		data[i], data[j] = data[j], data[i]
	}
	return data
}

// XORWithRandomNumber XORs the data with a random number.
func XORWithRandomNumber(data []byte) ([]byte, int, error) {
	randNum, err := rand.Int(rand.Reader, big.NewInt(256))
	if err != nil {
		return nil, 0, err
	}
	randByte := byte(randNum.Int64())
	for i := range data {
		data[i] ^= randByte
	}
	return data, int(randByte), nil
}

// PostFile posts a file to the server and returns the response.
func PostFile(filename string, targetURL string) ([]byte, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("file", filepath.Base(file.Name()))
	if err != nil {
		return nil, err
	}
	_, err = io.Copy(part, file)
	if err != nil {
		return nil, err
	}
	writer.Close()

	request, err := http.NewRequest("POST", targetURL, body)
	request.Header.Set("Content-Type", writer.FormDataContentType())
	if err != nil {
		return nil, err
	}

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return nil, err
	}

	return responseData, nil
}

func main() {
	// File to encrypt
	fileName := "filepenting"

	// Read the file
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatalf("Failed to read file: %v", err)
	}

	// Step 1: Reverse the file data
	data = ReverseBytes(data)

	// Step 2: Post the reversed file to the server
	encryptedData, err := PostFile(fileName, "http://localhost:8080/encrypt")
	if err != nil {
		log.Fatalf("Failed to post file: %v", err)
	}

	// Step 3: XOR the encrypted data with a random number
	finalData, randByte, err := XORWithRandomNumber(encryptedData)
	if err != nil {
		log.Fatalf("Failed to XOR data: %v", err)
	}
	fmt.Printf("XOR'd with random byte: %d\n", randByte)

	// Save the final data to a file
	err = ioutil.WriteFile("encrypted_"+fileName, finalData, 0644)
	if err != nil {
		log.Fatalf("Failed to write encrypted file: %v", err)
	}

	fmt.Println("File encryption completed successfully.")
}
