from Crypto.Random import get_random_bytes
import pandas as pd
from benchmark_cipher import *
#from datetime import datetime as timestamp
from utils import time

# Abrir arquivo
def open_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().encode('utf-8')
    except Exception as e:
        print(f"Erro ao abrir o arquivo {file_path}: {e}")
        return None


def run_benchmarks(files=[None], rounds=10):
    path = "src/data/"
    path_csv = "src/csv/"
    # Lista de resultados
    results = []
    rounds = rounds

    for file in files:
        original_data = path + file
        content = open_file(original_data)
        if content is None:
            continue

        # Gerar chaves e IV/nonce
        aes_key = get_random_bytes(16)      # AES-128
        aes_iv = get_random_bytes(AES.block_size)
        aes_nonce = get_random_bytes(8)
        chacha_key = get_random_bytes(32)   # ChaCha20
        chacha_nonce = get_random_bytes(8)

        # Benchmark AES e ChaCha20
        ecb_cipher, ecb_lat, ecb_thr = benchmark_encrypt("ECB", content, aes_key, runs=rounds)
        cbc_cipher, cbc_lat, cbc_thr = benchmark_encrypt("CBC", content, aes_key, aes_iv, runs=rounds)
        ctr_cipher, ctr_lat, ctr_thr = benchmark_encrypt("CTR", content, aes_key, aes_nonce, runs=rounds)
        chacha_cipher, chacha_lat, chacha_thr = benchmark_encrypt("ChaCha20", content, chacha_key, chacha_nonce, runs=rounds)

        # Decifragem
        ecb_dec_lat, ecb_dec_thr = benchmark_decrypt("ECB", ecb_cipher, aes_key, runs=rounds)
        cbc_dec_lat, cbc_dec_thr = benchmark_decrypt("CBC", cbc_cipher, aes_key, aes_iv, runs=rounds)
        ctr_dec_lat, ctr_dec_thr = benchmark_decrypt("CTR", ctr_cipher, aes_key, aes_nonce, runs=rounds)
        chacha_dec_lat, chacha_dec_thr = benchmark_decrypt("ChaCha20", chacha_cipher, chacha_key, chacha_nonce, runs=rounds)

        results.append({
            "Arquivo": file,
            "ECB_Latência(s)": ecb_lat,
            "ECB_Throughput(MB/s)": ecb_thr,
            "ECB_Decrypt_Latência(s)": ecb_dec_lat,
            "ECB_Decrypt_Throughput(MB/s)": ecb_dec_thr,
            "CBC_Latência(s)": cbc_lat,
            "CBC_Throughput(MB/s)": cbc_thr,
            "CBC_Decrypt_Latência(s)": cbc_dec_lat,
            "CBC_Decrypt_Throughput(MB/s)": cbc_dec_thr,
            "CTR_Latência(s)": ctr_lat,
            "CTR_Throughput(MB/s)": ctr_thr,
            "CTR_Decrypt_Latência(s)": ctr_dec_lat,
            "CTR_Decrypt_Throughput(MB/s)": ctr_dec_thr,
            "ChaCha20_Latência(s)": chacha_lat,
            "ChaCha20_Throughput(MB/s)": chacha_thr,
            "ChaCha20_Decrypt_Latência(s)": chacha_dec_lat,
            "ChaCha20_Decrypt_Throughput(MB/s)": chacha_dec_thr
        })

    # Salvar CSV
    df = pd.DataFrame(results)
    #time = timestamp.now().strftime("%Y%m%d_%H%M%S")
    csv_file = path_csv+f"{rounds}_benchmark_crypto_{time}.csv"
    df.to_csv(csv_file, index=False)
    print(f"Resultados salvos em {csv_file}")
    return csv_file