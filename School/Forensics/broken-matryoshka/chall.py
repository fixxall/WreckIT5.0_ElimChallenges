import zipfile
import os

def compress_file(input_file, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        zipf.write(input_file, os.path.basename(input_file))

def edit_hex(zip_file):
    with open(zip_file, 'r+b') as f:
        f.seek(0)
        f.write(b'\x00\x00\x00\x00\x00')

def main():
    input_filename = 'flag'
    current_file = input_filename

    for i in range(1, 101):
        zipname = f'{i}.zip'
        compress_file(current_file, zipname)
        edit_hex(zipname)
        current_file = zipname

if __name__ == "__main__":
    main()
