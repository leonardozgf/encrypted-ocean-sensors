import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_utils import CryptoUtils

def test_crypto_utils():
    key = b'secret_key'
    data = b'Test message'
    crypto = CryptoUtils(key)
    
    encrypted_data = crypto.encrypt(data)
    decrypted_data = crypto.decrypt(encrypted_data)
    
    assert decrypted_data == data
