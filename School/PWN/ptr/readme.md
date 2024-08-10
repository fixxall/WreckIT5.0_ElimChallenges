# *ptr

Author: Sanapati Cyberstorm

## Description

Mari kita bermain dengan pointer

## Requirements

None

## Sources

-

## Tags

pointer, canary

## Exploit

Program ini memiliki mitigasi Canary, dan juga merupakan PIE (Position Independent Executable).
Jadi yang harus kita lakukan adalah leak canary dari fungsi strstr, satisfy canary check, dan overwrite
Instruction Pointer (RIP) menjadi address 0x40127e untuk mendapatkan Arbitrary Code Execution

## Flag

```
WRECKIT50{the_p01nt3r_l3akS_th3_can4ry}
```

## connection


## Severity
MEDIUM
