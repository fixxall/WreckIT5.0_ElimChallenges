# SystemIntegration_STIs

Author: [wondPing](https://github.com/fixxall)

## Description

user: user

## Requirements

None

## Sources

- [dist](./dist)

## Tags

- SQli
- AES_CBC
- SSTI
- Sandbox Python

## Exploit

1. Blind SQL injection on login to get admin password / SEED
2. Using SSTI payload to cat the flag
3. Bypass filtering on SSTI payload (bypass sandboxing python)
4. Generate ciphertext for SSTI payload using choosen ciphertext attack on AES_CBC

- [solution](./solution)

## Flag

```bash
WRECKIT50{JanganLupaSetelah_DevAPP_UjiTestCase!!}
```

## connection

http://188.166.247.108:7014/

## Severity

MEDIUM
