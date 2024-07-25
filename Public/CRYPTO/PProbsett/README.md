# Desa NIistik

Author: [wondPing](https://github.com/fixxall)

## Description

RO adalah seorang kepala desa yang sangat populer. Hal itu disebabkan karena perilaku dan sikapnya. Stabil, tetap, konsisten dan teratur serta beraturan menjadi hal yang mendasarinya dalam menjadi kepala desa. Dari situ terdapat syarat untuk masuk desa RO, yaitu dengan melakukan 32x autentikasi.

## Requirements

None

## Sources

- [dist](./dist)

## Tags

- ECDSA 
- secp256k1
- Failing serialization

## Exploit

- BruteForce private keys
- Collision header serialization secp256k1 module
- Deterministik on ecdsa

- [solution](./solution)

## Flag

```
WRECKIT50{Y34h_y0uu_kN00w1n9_d3terM1n15ttik_NOWW}
```

## connection

nc wreckit.com 50502

## Severity
EAZY

