from Crypto.Cipher import AES, ChaCha20
from Crypto.Util.Padding import pad
import time

# Benchmark cifragem
def benchmark_encrypt(mode, data, key, iv_or_nonce=None, runs=5):
    times = []
    for _ in range(runs):
        start = time.perf_counter()

        if mode == "ECB":
            cipher = AES.new(key, AES.MODE_ECB)
            encrypted = cipher.encrypt(pad(data, AES.block_size))

        elif mode == "CBC":
            cipher = AES.new(key, AES.MODE_CBC, iv_or_nonce)
            encrypted = cipher.encrypt(pad(data, AES.block_size))

        elif mode == "CTR":
            cipher = AES.new(key, AES.MODE_CTR, nonce=iv_or_nonce)
            encrypted = cipher.encrypt(data)

        elif mode == "ChaCha20":
            cipher = ChaCha20.new(key=key, nonce=iv_or_nonce)
            encrypted = cipher.encrypt(data)

        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    data_mb = len(data) / (1024 * 1024)
    throughput = data_mb / avg_time
    return encrypted, avg_time, throughput

# Benchmark decifragem
def benchmark_decrypt(mode, ciphertext, key, iv_or_nonce=None, runs=5):
    times = []
    for _ in range(runs):
        start = time.perf_counter()

        if mode == "ECB":
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)

        elif mode == "CBC":
            cipher = AES.new(key, AES.MODE_CBC, iv_or_nonce)
            decrypted = cipher.decrypt(ciphertext)

        elif mode == "CTR":
            cipher = AES.new(key, AES.MODE_CTR, nonce=iv_or_nonce)
            decrypted = cipher.decrypt(ciphertext)

        elif mode == "ChaCha20":
            cipher = ChaCha20.new(key=key, nonce=iv_or_nonce)
            decrypted = cipher.decrypt(ciphertext)

        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    data_mb = len(ciphertext) / (1024 * 1024)
    throughput = data_mb / avg_time
    return avg_time, throughput