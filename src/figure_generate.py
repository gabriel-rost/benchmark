import matplotlib.pyplot as plt
import pandas as pd
#from datetime import datetime as timestamp
from utils import time

def generate_comparative_figure(csv_file, rounds=10):
    path_fig="src/figures/"
    
    # Carregar dados do CSV
    df = pd.DataFrame(pd.read_csv(csv_file))

    # Gráficos
    plt.figure(figsize=(18, 7))

    # Latência: cifragem vs decifragem
    plt.subplot(1, 2, 1)
    width = 0.2  # largura das barras
    x = range(len(df["Arquivo"]))

    # Barras de cifragem
    plt.bar([i - 1.5*width for i in x], df["ECB_Latência(s)"], width=width, label="ECB Encrypt")
    plt.bar([i - 0.5*width for i in x], df["CBC_Latência(s)"], width=width, label="CBC Encrypt")
    plt.bar([i + 0.5*width for i in x], df["CTR_Latência(s)"], width=width, label="CTR Encrypt")
    plt.bar([i + 1.5*width for i in x], df["ChaCha20_Latência(s)"], width=width, label="ChaCha20 Encrypt")

    # Barras de decifragem (mesmo deslocamento, hatch)
    plt.bar([i - 1.5*width for i in x], df["ECB_Decrypt_Latência(s)"], width=width, hatch='//', alpha=0.5, label="ECB Decrypt")
    plt.bar([i - 0.5*width for i in x], df["CBC_Decrypt_Latência(s)"], width=width, hatch='//', alpha=0.5, label="CBC Decrypt")
    plt.bar([i + 0.5*width for i in x], df["CTR_Decrypt_Latência(s)"], width=width, hatch='//', alpha=0.5, label="CTR Decrypt")
    plt.bar([i + 1.5*width for i in x], df["ChaCha20_Decrypt_Latência(s)"], width=width, hatch='//', alpha=0.5, label="ChaCha20 Decrypt")

    plt.xticks(x, df["Arquivo"])
    plt.ylabel("Latência (s)")
    plt.title("Latência de Cifragem vs Decifragem")
    plt.legend(fontsize=8)

    # Throughput: cifragem vs decifragem
    plt.subplot(1, 2, 2)
    # Barras de cifragem
    plt.bar([i - 1.5*width for i in x], df["ECB_Throughput(MB/s)"], width=width, label="ECB Encrypt")
    plt.bar([i - 0.5*width for i in x], df["CBC_Throughput(MB/s)"], width=width, label="CBC Encrypt")
    plt.bar([i + 0.5*width for i in x], df["CTR_Throughput(MB/s)"], width=width, label="CTR Encrypt")
    plt.bar([i + 1.5*width for i in x], df["ChaCha20_Throughput(MB/s)"], width=width, label="ChaCha20 Encrypt")

    # Barras de decifragem
    plt.bar([i - 1.5*width for i in x], df["ECB_Decrypt_Throughput(MB/s)"], width=width, hatch='//', alpha=0.5, label="ECB Decrypt")
    plt.bar([i - 0.5*width for i in x], df["CBC_Decrypt_Throughput(MB/s)"], width=width, hatch='//', alpha=0.5, label="CBC Decrypt")
    plt.bar([i + 0.5*width for i in x], df["CTR_Decrypt_Throughput(MB/s)"], width=width, hatch='//', alpha=0.5, label="CTR Decrypt")
    plt.bar([i + 1.5*width for i in x], df["ChaCha20_Decrypt_Throughput(MB/s)"], width=width, hatch='//', alpha=0.5, label="ChaCha20 Decrypt")

    plt.xticks(x, df["Arquivo"])
    plt.ylabel("Throughput (MB/s)")
    plt.title("Throughput de Cifragem vs Decifragem")
    plt.legend(fontsize=8)

    plt.tight_layout()
    #time = timestamp.now().strftime("%Y%m%d_%H%M%S")
    fig_file = f"{path_fig}{rounds}_benchmark_crypto_comparativo_{time}.png"
    plt.savefig(fig_file)
    print(f"Gráfico comparativo salvo em {fig_file}")