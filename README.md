[![All Contributors](https://img.shields.io/badge/all_contributors-6-darkblue.svg?style=flat-square)](#contributors-)

# WreckIT 5.0 - Elimination CTF Challenge Environments

WreckIt CTF is an annual national cyber security competition organized by Badan Siber dan Sandi Negara (BSSN) in Indonesia.

On 2024, WreckIT For the preliminary stage, the competition format follows the Jeopardy style, where teams compete in various categories of challenges.

## Table of Contents

* [Usage](#Usage)
* [Format Flag](#Format-Flag)
* [List of Challenges](#List-of-Challenges)

## Usage

The installation steps of docker and docker-compose for others operating system might be slightly different, please refer to the [docker documentation](https://docs.docker.com/) for details.

Every service will use different port. To setting port use <code>docker-composer.yml</code> on every challenge.
```bash
git clone https://github.com/fixxall/WreckIT5.0_ElimChallenges.git

# Enter the directory of service. Example for p00-warmup:
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

- The flags must be enclosed in `WRECKIT50{}`.
- They can have numbers, alphabets, `_`s, `'`s, `!`s, `.`s, `+`s, `-`s, `@`s, `#`s, `$`s, `%`s, `:`s, `>`s.
- They must be related to the challenge.
- They must not be so simple that you can guess them.

Here's a regex for the flag format.

```
/^WRECKIT50{[\w_!@#?$%\.'"+:->]{5,50}}$/
```

Here's a sample flag.

```
WRECKIT50{hell0W_olrd_!5Simpl3#}
```

## List of Challenges on Public category

| No  | Category  | Challenge Name       | Author      |  Connection                                                 |
| --- | --------- | ------------------- | ----------- | ---------------------------------------------------- |
| 1   | Crypto    | example  | wondPing    | nc localhost 8088 |
