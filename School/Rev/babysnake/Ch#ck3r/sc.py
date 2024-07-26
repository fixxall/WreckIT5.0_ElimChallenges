## Gen Key
def process_hex_string(hex_string):
    keyhex = [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]
    for i in range(len(keyhex)):
        keyhex[i] = keyhex[i] ^ (i + 1)
    return keyhex

def reverse_process_hex_string(keyhex):
    for i in range(len(keyhex)):
        keyhex[i] = keyhex[i] ^ (i + 1)
    hex_string = ''.join([format(x, '02x') for x in keyhex])
    return hex_string

# Example usage
hex_string = "6c3374737772336b746833666c346721" #Original Key
hex_string2 = "7772336b6976666f72656e6372797074" #Original IV
result = process_hex_string(hex_string)
result2 = process_hex_string(hex_string2)
print("Processed key:", result) #Chall Key
print("Processed IV:", result2) #Chall IV

key = reverse_process_hex_string(result)
key2 = reverse_process_hex_string(result2)
print("recovered key:", key)
print("recovered IV:", key2)


## Gen Enc
def shuffle_hex_string(hex_string):
    even_chars = [hex_string[i] for i in range(len(hex_string)) if i % 2 == 0]
    odd_chars = [hex_string[i] for i in range(len(hex_string)) if i % 2 == 1]
    
    shuffled = ''.join(even_chars + odd_chars)
    return shuffled

def unshuffle_hex_string(shuffled_string):
    n = len(shuffled_string)
    half = (n + 1) // 2  # This is the size of the even indexed characters
    
    even_chars = shuffled_string[:half]
    odd_chars = shuffled_string[half:]
    
    original_chars = []
    for i in range(n):
        if i % 2 == 0:
            original_chars.append(even_chars[i // 2])
        else:
            original_chars.append(odd_chars[i // 2])
    
    return ''.join(original_chars)

original_hex = "e47ee11a101a1b2158b560454b6e588e7a8a5ffdffa44611c7534f90ac8bd2d4efa1b66d153914c86af0655c59bc2934"
shuffled_hex = shuffle_hex_string(original_hex)
print("Shuffled Hex:", shuffled_hex)

unshuffled_hex = unshuffle_hex_string(shuffled_hex)
print("Unshuffled Hex (should match original):", unshuffled_hex)


## WRECKIT50{C#_and_d0tNET_e4sy_Rev3rs3}


# Solve
from Crypto.Cipher import AES
import binascii

def decrypt_aes_cbc(encrypted_hex, key, iv):
    key_bytes = bytes(key)
    iv_bytes = bytes(iv)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    encrypted_bytes = binascii.unhexlify(encrypted_hex)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes

# Decrypt the unshuffled hex string
key = [int(x) for x in result]
iv = [int(x) for x in result2]
decrypted_bytes = decrypt_aes_cbc(unshuffled_hex, key, iv)
print("Decrypted message:", decrypted_bytes)
