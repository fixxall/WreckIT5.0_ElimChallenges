## chall:
dist.rar

## deskripsi:
just simple rev

## Poc:
chall dienkripsi dengan skema:
-cek total hex byte dari file inputan apakah kelipatan 8, jika tidak berikan padding hingga total hex byte kelipatan 8
-generate kunci xor dari 4 byte pertama dari file inputan dixor dengan 4 byte selanjutnya
(byte 1, byte 2, byte 3, byte 4) xor dengan (byte 5, byte 6, byte 7, byte 8) = 4 byte kunci xor

karena diketahui file itu formatnya .png
yang mana 8 byte pertama dari filenya adalah:
89 50 4E 47 0D 0A 1A 0A

tinggal generate key xornya
(byte 1, byte 2, byte 3, byte 4) xor dengan (byte 5, byte 6, byte 7, byte 8) = 4 byte kunci xor

## flag:
``` WRECKIT50{junior's_f1rst_revers4l} ```
