import math
import time
from collections import defaultdict

# Fungsi penunjuang
def float_bin(my_number, places=3): 
    my_whole, my_dec = str(my_number).split(".")
    my_whole = int(my_whole)
    res = (str(bin(my_whole))+".").replace('0b','')

    for x in range(places):
        my_dec = str('0.')+str(my_dec)
        temp = '%1.20f' % (float(my_dec) * 2)
        my_whole, my_dec = temp.split(".")
        res += my_whole
    return res

def cyclic_left_shift(value, shift):
    return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))

def int_to_bit(integer):
    if integer < 0:
        raise ValueError("Bilangan bulat harus non-negatif")
    return bin(integer)[2:]

def binary32(n): 
    sign = 0
    if n < 0: 
        sign = 1
        n = n * (-1) 
    p = 30
    dec = float_bin(n, places= p)

    dotPlace = dec.find('.')
    onePlace = dec.find('1')

    if onePlace > dotPlace:
        dec = dec.replace(".","")
        onePlace -= 1
    elif onePlace < dotPlace:
        dec = dec.replace(".","")
        dotPlace -= 1
    mantissa = dec[onePlace+1:]

    exponent = dotPlace - onePlace
    exponent_bits = exponent + 127

    exponent_bits = bin(exponent_bits).replace("0b",'') 

    mantissa = mantissa[0:23]

    final = str(sign) + exponent_bits.zfill(8) + mantissa
    return final

# Fungsi utama
def parse_input(x):
    if len(x) != 32:
        raise ValueError("Input harus 32-bit string")
    
    xl = x[:12]
    xm = x[12:28]
    xr = x[28:]
    
    return xl, xm, xr

def calculate_parameters(xl, xm, xr):
    gama_awal = int(xl, 2) * (1 / 2**12)
    eta = (int(xm, 2) * (2 / 2**16)) + 2
    k = (int(xr, 2) * (1 / 2**4)) + 10.01
    n = math.floor(6 * gama_awal)
    
    return gama_awal, eta, k, n

def fL(eta, gama_n):
    return eta * gama_n * (1 - gama_n)

def gamma_function(gama_awal, eta, k, n, i):
    gama = gama_awal
    for _ in range(n + i):
        gama = (2**k / 2**fL(eta, gama)) % 1
    return gama

def ELM(x):
    xl, xm, xr = parse_input(x)
    gama_awal, eta, k, n = calculate_parameters(xl, xm, xr)
    
    gama_n1 = gamma_function(gama_awal, eta, k, n, 1)
    gama_n2 = gamma_function(gama_awal, eta, k, n, 2)
    
    w1 = binary32(gama_n1 * (10**(10)))
    w2 = binary32(gama_n2)
    y = (cyclic_left_shift(int(w1, 2), 17)) ^ (int(w2, 2))
    return format(y, '032b')

# Cari nilai x yang menghasilkan nilai y yang sama
total_iterations = 2 ** 32  # Jumlah total iterasi yang akan dilakukan
progress_step = total_iterations // 100  # Langkah progres untuk menampilkan persentase
progress = 0

start_time = time.time()

collision_dict = defaultdict(list)

for i in range(total_iterations):
    if i % progress_step == 0 and i > 0:
        elapsed_time = time.time() - start_time
        print(f"Progress: {progress}%, Waktu berlalu: {elapsed_time:.2f} detik")
        
        # Simpan hasil kolisi ke dalam file teks
        with open(f'collisions_{progress}percent.txt', 'w') as f:
            for y, x_list in collision_dict.items():
                if len(x_list) > 1:
                    f.write(f"kolisi dari nilai y: {y} adalah x = {x_list}\n")
        
        # Kosongkan collision_dict untuk iterasi berikutnya
        collision_dict = defaultdict(list)
        
        progress += 1
    
    x = format(i, '032b')
    y = ELM(x)
    collision_dict[y].append(x)

# Simpan hasil kolisi terakhir ke dalam file teks
with open(f'collisions_{progress}percent.txt', 'w') as f:
    for y, x_list in collision_dict.items():
        if len(x_list) > 1:
            f.write(f"kolisi dari nilai y: {y} adalah x = {x_list}\n")

print("Hasil kolisi telah disimpan di file-file collisions_*.txt")
