def read_binary_file_as_binary_string(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string

def convert_binary_string_to_hex(binary_string):
    hex_string = ''
    for i in range(0, len(binary_string), 4):
        hex_digit = binary_string[i:i+4]
        hex_string += format(int(hex_digit, 2), 'x')
    return hex_string

def write_hex_string_to_binary_file(hex_string, output_file_path):
    byte_data = bytearray.fromhex(hex_string)
    with open(output_file_path, 'wb') as file:
        file.write(byte_data)

# Contoh penggunaan
input_file_path = 'output_file.bin'  # File input yang berisi angka biner 0 dan 1
output_file_path = 'output.bin'  # File output yang akan berisi data hex dalam mode binary

# Membaca file dan mengonversi ke string biner
binary_string = read_binary_file_as_binary_string(input_file_path)
print(f"Biner string: {binary_string}")

# Mengonversi string biner ke string hex
hex_string = convert_binary_string_to_hex(binary_string)
print(f"Hex string: {hex_string}")

# Menulis string hex ke file binary
write_hex_string_to_binary_file(hex_string, output_file_path)
print(f"Hex string telah ditulis ke {output_file_path} sebagai data binary")
