from data_generate import generate_data
from benchmark_configs import run_benchmarks
from figure_generate import generate_comparative_figure
from utils import time

# Configurações
files = [f"file_10MB_{time}.txt", f"file_50MB_{time}.txt", f"file_100MB_{time}.txt"]
size_in_mb = [10, 50, 100]
rounds = 10

# Gerar arquivos de dados
print("Gerando arquivos de dados...")
generate_data(files[0], size_in_mb[0])
generate_data(files[1], size_in_mb[1])
generate_data(files[2], size_in_mb[2])
print("Arquivos de dados gerados.")

# Executar benchmarks
print("Executando benchmarks...")
dir = run_benchmarks(files, rounds)
print("Benchmarks concluídos.")

# Gerar figuras comparativas
print("Gerando figuras comparativas...")
generate_comparative_figure(dir, rounds)
print("Figuras geradas.")
print("Processo concluído.")