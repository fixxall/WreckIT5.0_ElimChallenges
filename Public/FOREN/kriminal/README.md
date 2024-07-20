# kriminal

Author: [hanz0](https://github.com/rayhanhanaputra)

## Description

Akhirnya, pengedar narkoboy telah tertangkap. Tapi bukti-buktinya mana ya???
Flag adalah address cryptowallet pengedar, wrap pakai WRECKIT50{}

https://drive.google.com/file/d/19iCeuRW-DAhY3WsxwHvNLehxCZR7tewl/view?usp=drive_link
Password zip: n0#brutbrut#b0z

## Hint

Hint 1 = https://github.com/oxen-io/session-android
Hint 2 = Session adalah hasil fork dari Signal

## Sources

- [dist](./dist)

## Tags

- Mobile Forensic, Reverse

## Exploit

Get the key to decrypt database key from
/data/data/network.loki.messenger/shared_prefs/network.loki.messenger_preferences.xml
/data/misc/keystore/persistent.sqlite

key 85d07b0feea17ca9dc44659b7ef59cf4
input 1568840ea8875852b1a1d9f4e24c38174f7410e87dc08f940d00903ee417a846
gcm 018e4f10396b8e38c8b7543b60413e5d
iv c+pVgZB3E9xeZB3H

final key dca543d343fc273b37d31fa9df90762a010151474429c899fbe8b8b76a539186

## Flag

```
WRECKIT50{0x1ABC7154748D1CE5144478CDEB574AE244B939B4}
```

## Severity

HARD
