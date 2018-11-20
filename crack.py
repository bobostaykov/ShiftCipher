from collections import defaultdict
import math

from encrypt_decrypt import decrypt

real_frequencies = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.043,
    'e': 0.127,
    'f': 0.022,
    'g': 0.020,
    'h': 0.061,
    'i': 0.070,
    'j': 0.002,
    'k': 0.008,
    'l': 0.040,
    'm': 0.024,
    'n': 0.067,
    'o': 0.015,
    'p': 0.019,
    'q': 0.001,
    'r': 0.060,
    's': 0.063,
    't': 0.091,
    'u': 0.028,
    'v': 0.010,
    'w': 0.024,
    'x': 0.002,
    'y': 0.020,
    'z': 0.001,
}


def compute_letter_count(text):
    letter_count = defaultdict(int)
    for char in text:
        letter_count[char] += 1
    return letter_count


def compute_frequencies(text):
    letter_frequencies = {}
    letter_count = compute_letter_count(text)
    leng = len(text)
    for char in range(ord('a'), ord('z') + 1):
        letter_frequencies[chr(char)] = letter_count[chr(char)] / leng
    return letter_frequencies


cipher = input("Cipher text: ")

cipher_frequencies = compute_frequencies(cipher)


def sum_frequencies_squared(key):
    sum = 0
    for char in range(ord('a'), ord('z') + 1):
        if char + key > 122:
            sum += real_frequencies[chr(char)] * cipher_frequencies[chr(char + key - 26)]
        else:
            sum += real_frequencies[chr(char)] * cipher_frequencies[chr(char + key)]
    return sum


min_diff = math.inf
real_key = 0

for possible_key in range(0, 26):
    sum_freq_sq = sum_frequencies_squared(possible_key)
    if abs(sum_freq_sq - 0.065) < min_diff:
        min_diff = abs(sum_freq_sq - 0.065)
        real_key = possible_key

print("\nKey : " + str(real_key))
print("\nPlain text: " + decrypt(real_key, cipher))













