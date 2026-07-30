from itertools import cycle

source_xor = "bytes(a ^ b for a, b in zip(data, __import__('itertools').cycle(key)))"

def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, cycle(key)))