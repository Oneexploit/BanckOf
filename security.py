# security.py
from Crypto.Cipher import AES
import base64

# تابع برای رمزنگاری اطلاعات
def encrypt_data(data, secret_key):
    cipher = AES.new(secret_key.encode('utf-8'), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.encodebytes(cipher.nonce + tag + ciphertext).decode('utf-8')

# تابع برای رمزگشایی اطلاعات
def decrypt_data(encrypted_data, secret_key):
    data = base64.decodebytes(encrypted_data.encode('utf-8'))
    cipher = AES.new(secret_key.encode('utf-8'), AES.MODE_EAX, nonce=data[:16])
    decrypted_data = cipher.decrypt_and_verify(data[32:], data[16:32])
    return decrypted_data.decode('utf-8')

# مثال استفاده
if __name__ == '__main__':
    secret_key = 'ThisIsASecretKey'
    original_data = 'Sensitive Data'

    encrypted_data = encrypt_data(original_data, secret_key)
    print(f"Encrypted: {encrypted_data}")

    decrypted_data = decrypt_data(encrypted_data, secret_key)
    print(f"Decrypted: {decrypted_data}")
