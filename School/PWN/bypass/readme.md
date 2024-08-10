# Bypass

Author: Sanapati Cyberstorm

## Description

Passwordnya apa man?

## Requirements

None

## Sources

-

## Tags

nullbyte

## Exploit

Program meminta kita untuk menginput password yang ukuran maksimalnya empat bytes, kemudian password kita akan dibandingkan dengan string “apayah” yang ukurannya enam bytes. Jika sama, maka program akan menampilkan flag di layar dengan fungsi apatuh. Fungsi strcmp berhenti melakukan comparison ketika menemukan nullbyte (\x00 atau \0), jadi cukup kirim nullbyte sebanyak 4 bytes agar fungsi strcmp tidak melakukan comparison.

## Flag

```
WRECKIT50{3zzz_byp4ss_on_my_pr0gr4m}
```
## connection



## Severity
MEDIUM
