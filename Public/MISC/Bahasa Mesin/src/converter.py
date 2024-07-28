def read_file_as_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_content = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_content)
    return binary_string

def write_binary_string_to_file(binary_string, output_file_path):
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    with open(output_file_path, 'wb') as file:
        file.write(byte_array)

def write_binary_string_to_text_file(binary_string, text_file_path):
    with open(text_file_path, 'w') as file:
        file.write(binary_string)

def read_binary_string_from_text_file(text_file_path):
    with open(text_file_path, 'r') as file:
        binary_string = file.read()
    return binary_string

# Contoh penggunaan
input_file_path = '32'
binary_text_file_path = 'binary_string.txt'
output_file_path = 'output_file.bin'

# Membaca file dan mengonversi ke string biner
binary_string = read_file_as_binary_string(input_file_path)
print(f"Biner string: {binary_string}")

# Menulis string biner ke file teks
write_binary_string_to_text_file(binary_string, binary_text_file_path)
print(f"Biner string telah ditulis ke {binary_text_file_path}")

# Membaca string biner dari file teks
binary_string_from_file = read_binary_string_from_text_file(binary_text_file_path)
print(f"Biner string yang dibaca dari file teks: {binary_string_from_file}")

# Menulis string biner kembali ke file binary
write_binary_string_to_file(binary_string_from_file, output_file_path)
print(f"Biner string telah ditulis kembali ke file binary {output_file_path}")
