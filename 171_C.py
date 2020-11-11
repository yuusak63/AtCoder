import sys
import math

N = int(input())

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
result = []

def alphabet_decimal(N):
    quotient = math.floor(N / len(ALPHABET))
    surplus = N % len(ALPHABET)
    quotient -= 1 if surplus == 0 else 0
    surplus = len(ALPHABET) if surplus == 0 else surplus
    result.append(surplus)
    if len(ALPHABET) < quotient:
        alphabet_decimal(quotient)
    elif len(ALPHABET) < N:
        result.append(quotient)
    return "".join([ALPHABET[i - 1] for i in reversed(result)])

print(alphabet_decimal(int(N)))
