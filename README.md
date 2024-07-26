# WreckIT 5.0 - Elimination CTF Challenge Environments

[![All Contributors](https://img.shields.io/badge/all_contributors-6-darkblue.svg?style=flat-square)](#contributors-)

WreckIt CTF is an annual national cyber security competition organized by Badan Siber dan Sandi Negara (BSSN) in Indonesia.

On 2024, WreckIT For the preliminary stage, the competition format follows the Jeopardy style, where teams compete in various categories of challenges.

## Table of Contents

* [Usage](## Usage)
* [Format Flag](## Format-Flag)
* [List of Challenges](## List-of-Challenges)

## Usage

The installation steps of docker and docker-compose for others operating system might be slightly different, please refer to the [docker documentation](https://docs.docker.com/) for details.

Every service will use different port. To setting port use <code> docker-composer.yml </code> on every challenge.

```bash
git clone https://github.com/fixxall/WreckIT5.0_ElimChallenges.git

# Enter the directory of service. Example CRYPTO/example:
cd CRYPTO/example

# Compile environment
docker-compose build

# Run environment
docker-compose up -d
```

Delete / turn off service.

```bash
docker-compose down -v
```

## Format Flag

1. The flags must be enclosed in `WRECKIT50{}`.
2. They can have numbers, alphabets, `_`s, `'`s, `!`s, `.`s, `+`s, `-`s, `@`s, `#`s, `$`s, `%`s, `:`s, `>`s.
3. They must be related to the challenge.
4. They must not be so simple that you can guess them.

Here's a regex for the flag format.

```bash
/^WRECKIT50{[\w_!@#?$%\.'"+:->]{5,50}}$/
```

Here's a sample flag.

```bash
WRECKIT50{hell0W_olrd_!5Simpl3#}
```

## List of Challenges on Public category

| No  | Category  | Challenge Name       | Author      |  Connection    |
| --- | --------- | ------------------- | ----------- | ---------------- |
| 1   | Forensic    | The Magic of Word  | aodreamer    | - |
| 2   | Forensic    | KliptoLogie  | aodreamer    | - |
| 3   | Forensic    | kriminal  | hanz0    | - |
| 4   | Forensic    | -  | VascoZ    | - |
| 5   | Web    | Survey Pemerintah  | rafliher    | nc localhost 8088 |
| 6   | Web    | oshiku  | VascoZ    | nc localhost 8088 |
| 7   | Web    | WotaButa  | VascoZ    | nc localhost 8088 |
| 8   | Web    | SystemIntegration_SITs  | wondPing    | nc localhost 8088 |
| 9   | Pwn    | s1mple  | hanz0    | nc localhost 7021 |
| 10   | Pwn    | slim  | hanz0    | nc localhost 7022 |
| 11   | Pwn    | Kernel 1  | komang    | nc localhost 7023 |
| 12   | Pwn    | Kernel 2  | komang    | nc localhost 7024 |
| 13   | Reverse    | Just Simple Encryption  | rafliher    | - |
| 14   | Reverse    | Its About Time  | rafliher    | - |
| 15   | Reverse    | Aplikasi Berbasis Objek  | aodreamer    | - |
| 16   | Reverse    | Not Secure PDNS  | hanz0    | nc localhost 7034 |
| 17   | Crypto    | Easy RSA  | KING-Ace    | - |
| 18   | Crypto    | m4K c0MbL4n6  | KING-Ace    | - |
| 19   | Crypto    | Desa Nistik  | wondPing    | nc localhost 7043 |
| 20   | Crypto    | PProbsett  | wondPing    | nc localhost 7044 |
| 22   | Misc    | Bahasa Mesin   | wondPing    | - |
| 21   | Misc    | Aya's Number 2  | wondPing    | nc localhost 7052 |
| 23   | Misc    | Feedback  | -    | - |

## List of Challenges on School category

| No  | Category  | Challenge Name       | Author      |  Connection                                                 |
| --- | --------- | ------------------- | ----------- | ---------------------------------------------------- |
| 1   | Forensic    | bipbop  | k.eii    | - |
| 2   | Forensic    | broken-matryoshka  | k.eii    | - |
| 3   | Forensic    | pcapers  | k.eii    | - |
| 4   | Forensic    | puisi  | k.eii    | - |
| 5   | Reverse    | babysnake  | k.eii    | - |
| 6   | Reverse    | Ch#ck3r  | k.eii    | - |
| 7   | Reverse    | finitstedt  | k.eii    | - |
| 8   | Reverse    | letsgo  | k.eii    | - |
| 9   | Web    | Cheemsweb  | k.eii    | - |
| 10   | Web    | -  | -    | - |
| 11   | Web    | -  | -    | - |
| 12   | Web    | -  | -    | - |
| 13   | Pwn    | -  | -    | - |
| 14   | Pwn    | -  | -    | - |
| 15   | Pwn    | -  | -    | - |
| 16   | Pwn    | -  | -    | - |
| 17   | Crypto    | -  | -    | - |
| 18   | Crypto    | -  | -    | - |
| 19   | Crypto    | -  | -    | - |
| 20   | Crypto    | -  | -    | - |
