def decrypt_xor(ciphertext, key):
    key_len = len(key)
    decrypted = bytearray(len(ciphertext))
    for i in range(len(ciphertext)):
        decrypted[i] = ciphertext[i] ^ key[i % key_len]
    return bytes(decrypted)

def main():
    input_file = 'flagenc'
    output_file = 'decrypted_flag.txt'
    
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    
    key = './wrek1t'.encode('utf-8')
    print(f"Key: {key}")

    decrypted_data = decrypt_xor(ciphertext, key)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    
    print("Decryption successful!")
    print(decrypted_data)

if __name__ == "__main__":
    main()
