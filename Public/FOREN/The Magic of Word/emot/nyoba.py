import binascii

def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

for i in range(10):
    filename = f"emoji  ({i+1}).txt"
    f = open(filename,'r').read()
    print(filename)
    print(f)
    print(CRC32_from_file(filename))