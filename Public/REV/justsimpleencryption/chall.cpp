#include <iostream>
#include <string>
#include <bitset>   
#include <cstdbool>
#include <vector>
#include <sstream> 

using namespace std;

const int BLOCK_SIZE = 128;
const int BYTE_COUNT = BLOCK_SIZE / 8;
const int NIBBLE_SIZE = 4;
const int NIBBLE_COUNT = BLOCK_SIZE / NIBBLE_SIZE;
const int ROUND_NUMBER = 10;

bitset<4> roundKeys[ROUND_NUMBER][NIBBLE_COUNT];
bitset<4> buffer[NIBBLE_COUNT];

int mod(int a, int b){
    return (b + (a % b)) % b;
}

void chrstouint4s(string charArray, bitset<4> *uint4Array, int arraySize) {
    for (int i = 0; i < arraySize; ++i) {
        for (int j = 0; j < 2; ++j) {
            uint4Array[i * 2 + j] = bitset<4>((charArray[i] >> (8 - (j + 1) * 4)) & 0x0F);
        }
    }
}

void stringXor(bitset<4> *buffer, bitset<4> *k) {
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        buffer[i] ^= k[i];
    }
}

void indexShiftAdd(bitset<4> *buffer, int shiftNum) {
    bitset<4> temp[NIBBLE_COUNT];
    bitset<4> temp2[NIBBLE_COUNT];
    shiftNum = shiftNum % 2 ? shiftNum : shiftNum + 1;
    
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        if(i % 2 == 0)
            temp[i] = (buffer[i].to_ulong() + buffer[(i + shiftNum) % NIBBLE_COUNT].to_ulong()) % 16;
        else
            temp[i] = buffer[i].to_ulong() ^ buffer[(i + shiftNum) % NIBBLE_COUNT].to_ulong();
    }
    
    temp[shiftNum] = buffer[shiftNum];
    temp2[0] = temp[0];
    
    for (int i = 1; i < NIBBLE_COUNT; i++) {
        temp2[i] = temp[i] ^ temp[i - 1];
    }
    
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        buffer[i] = temp2[i];
    }
}

void indexShiftTrans(bitset<4> *buffer, int shiftNum) {
    bitset<4> temp[NIBBLE_COUNT];
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        temp[i] = buffer[(i + shiftNum) % NIBBLE_COUNT];
    }
    
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        buffer[i] = temp[i];
    }
}

int calcSum(bitset<4> *nibbles) {
    int sum = 0;
    for (int i = 0; i < NIBBLE_COUNT; i++) {
        sum += nibbles[i].to_ulong();
    }
    return sum % NIBBLE_COUNT;
}

string pkcs7Padding(string plain) {
    int padLen = BYTE_COUNT - (plain.length() % BYTE_COUNT);
    plain.append(padLen, static_cast<char>(padLen));
    return plain;
}

void prepareRoundKeys(string key) {
    if (key.length() < BYTE_COUNT) {
        key.append(BYTE_COUNT - key.length(), 'F');
    }
    chrstouint4s(key, roundKeys[0], BYTE_COUNT);

    for (int i = 0; i < NIBBLE_COUNT; i++) {
        roundKeys[1][i] = roundKeys[0][NIBBLE_COUNT - i - 1];
    }
    for (int i = 2; i < ROUND_NUMBER; i++) {
        for (int j = 0; j < NIBBLE_COUNT; j++) {
            roundKeys[i][j] = roundKeys[i - 1][(j + 1) % BYTE_COUNT] ^ roundKeys[i - 2][(j + 2) % BYTE_COUNT];
        }
    }
}

string encryptBlock(string plainBlock) {
    chrstouint4s(plainBlock, buffer, BYTE_COUNT);

    for (int k = 0; k < ROUND_NUMBER; k++) {
        stringXor(buffer, roundKeys[k]);
        indexShiftAdd(buffer, calcSum(roundKeys[k]));
        indexShiftTrans(buffer, calcSum(buffer));
    }

    string encrypted;
    encrypted.reserve(NIBBLE_COUNT / 2);
    for (int i = 0; i < NIBBLE_COUNT; i+=2) {
        encrypted += static_cast<char>((buffer[i].to_ulong() << 4) | buffer[i + 1].to_ulong());
    }
    return encrypted;
}

string encrypt(string plain, string key) {
    plain = pkcs7Padding(plain);
    prepareRoundKeys(key);

    string encrypted;
    for (size_t i = 0; i < plain.length(); i += BYTE_COUNT) {
        encrypted += encryptBlock(plain.substr(i, BYTE_COUNT));
    }
    return encrypted;
}


string hexValuesToString(const vector<string>& hexValues) {
    string result;
    result.reserve(hexValues.size()); // Reserve space to avoid multiple allocations

    for (const auto& hexValue : hexValues) {
        // Convert the hex string to an integer
        unsigned int charValue;
        stringstream ss;
        ss << hex << hexValue;
        ss >> charValue;

        // Append the character to the result string
        result += static_cast<char>(charValue);
    }

    return result;
}

int main() {
    string key = ".;D,AWo,asdfnpwe";
    string plain;
    cin >> plain;

    string encrypted = encrypt(plain, key);

    vector<string> hexValues = {
"e1", "fa", "1f", "2b", "e5", "1b", "59", "a2", "7f", "bb", "17", "25", "32", "40", "e2", "cd", "b3", "3e", "6c", "54", "18", "d9", "54", "d", "8e", "3", "89", "e1", "e4", "bd", "ff", "e4", "b2", "97", "d4", "b5", "2b", "73", "66", "31", "6d", "e7", "31", "c5", "d1", "9a", "25", "b5", "10", "d5", "d2", "c0", "c5", "2d", "90", "4f", "f0", "a1", "2d", "ad", "b6", "d6", "a1", "61"
    };

    string result = hexValuesToString(hexValues);

    if (result.compare(encrypted) == 0){
        cout << "Cakep";
    } else {
        cout << "Salah";
    }
    
    return 0;
}
