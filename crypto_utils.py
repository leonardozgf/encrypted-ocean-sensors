from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

class CryptoUtils:
    def __init__(self, key: bytes):
        self.key = hashlib.sha256(key).digest()
        self.block_size = AES.block_size

    def encrypt(self, data: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, self.block_size))
        return cipher.iv + ct_bytes

    def decrypt(self, data: bytes) -> bytes:
        iv = data[:self.block_size]
        ct = data[self.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), self.block_size)
        return pt
