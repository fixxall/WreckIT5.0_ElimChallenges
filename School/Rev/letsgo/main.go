package main

import (
    "fmt"
    "io/ioutil"
    "os"
)

func getKeyFromFileName(filename string) ([]byte, error) {
    if len(filename) == 0 {
        return nil, fmt.Errorf("filename is empty")
    }
    key := []byte(filename)
    return key, nil
}

func encryptXOR(data []byte, key []byte) []byte {
    keyLen := len(key)
    encrypted := make([]byte, len(data))
    for i := 0; i < len(data); i++ {
        encrypted[i] = data[i] ^ key[i%keyLen]
    }
    return encrypted
}

func main() {
    if len(os.Args) != 3 {
        fmt.Println("Usage: <input-file> <output-file>")
        return
    }

    inputFile := os.Args[1]
    outputFile := os.Args[2]

    data, err := ioutil.ReadFile(inputFile)
    if err != nil {
        fmt.Println("Error reading input file:", err)
        return
    }

    key, err := getKeyFromFileName(os.Args[0])
    if err != nil {
        fmt.Println("Error getting key from filename:", err)
        return
    }

    encryptedData := encryptXOR(data, key)

    err = ioutil.WriteFile(outputFile, encryptedData, 0644)
    if err != nil {
        fmt.Println("Error writing output file:", err)
        return
    }

    fmt.Println("Encryption successful!")
}
