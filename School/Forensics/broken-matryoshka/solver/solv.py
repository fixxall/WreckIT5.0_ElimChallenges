import zipfile
import os
import shutil

def edit_hex(zip_file):
    with open(zip_file, 'r+b') as f:
        f.seek(0)
        f.write(b'\x50\x4B\x03\x04\x14')

def extract_zip(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def main():
    current_zip = '100.zip'
    extract_path = 'extracted'
    temp_extract_path = 'temp_extracted'

    # Buat direktori ekstraksi jika belum ada
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    
    while True:
        try:
            # Edit 5 byte pertama dari file zip
            edit_hex(current_zip)

            # Bersihkan direktori ekstraksi sementara
            if os.path.exists(temp_extract_path):
                shutil.rmtree(temp_extract_path)
            os.makedirs(temp_extract_path)

            # Ekstrak konten
            extract_zip(current_zip, temp_extract_path)
            
            # Cari file zip berikutnya
            extracted_files = os.listdir(temp_extract_path)
            next_zip = None
            for file in extracted_files:
                if file.endswith('.zip'):
                    next_zip = os.path.join(temp_extract_path, file)
                    break

            if not next_zip:
                print("No more zip files found.")
                break

            # Pindahkan file zip berikutnya ke direktori utama untuk iterasi berikutnya
            current_zip = next_zip
            shutil.move(current_zip, os.path.join(extract_path, os.path.basename(current_zip)))
            current_zip = os.path.join(extract_path, os.path.basename(current_zip))

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
