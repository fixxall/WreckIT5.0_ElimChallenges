def swap_hex_values(input_file, output_file):
    # Read the binary data from the input file
    with open(input_file, 'rb') as f:
        data = f.read()

    # Convert the binary data to a hex string
    hex_data = data.hex()

    # Add padding if the length is odd
    if len(hex_data) % 2 != 0:
        hex_data += '00'

    # Swap the hex values
    swapped_hex = ''
    for i in range(0, len(hex_data), 4):
        swapped_hex += hex_data[i+2:i+4] + hex_data[i:i+2]

    # Convert the swapped hex string back to binary data
    swapped_data = bytes.fromhex(swapped_hex)

    # Write the binary data to the output file
    with open(output_file, 'wb') as f:
        f.write(swapped_data)

# Example usage
input_file = 'acdrnao.png'
output_file = 'result.png'
swap_hex_values(input_file, output_file)
