import os
from faker import Faker
fake = Faker('pt-BR')

path = "src/data/"

# Criar o arquivo dentro da pasta data
def create_file(file_name = "myfile.txt", method = "w"):
    '''
    method = 
    "x" - Create - will create a file, returns an error if the file exists
    "a" - Append - will create a file if the specified file does not exists
    "w" - Write - will create a file if the specified file does not exists
    '''
    print(path + file_name)
    f = open(path + file_name, method)
    f.close()

# Escrever no arquivo
def write_file(file_name = "myfile.txt", method = "a", lines = 10):
    '''
    method = 
    "a" - Append - will append to the end of the file
    "w" - Write - will overwrite any existing content
    '''
    f = open(path + file_name, method)
    for _ in range(lines):
        f.write(fake.name() + "\n")
    f.close()

# Checar o tamanho do arquivo
def check_file_size(file_path = "myfile.txt"):
    '''
    Check the size of a file in megabytes.
    '''
    file_size = os.path.getsize(path + file_path)
    return file_size / (1024 * 1024)

# Gerar dados até o arquivo atingir um tamanho específico
def generate_data(file_name = "myfile.txt", size_in_mb = 1):
    '''
    Generate a file with random data.
    '''
    create_file(file_name)
    write_file(file_name, lines=100)
    file_size = check_file_size(file_name)

    if file_size < size_in_mb:
        while file_size < size_in_mb:
            write_file(file_name, lines=100)
            file_size = check_file_size(file_name)
            print(f"Current file size: {file_size:.2f} MB")
    print(f"Final file size: {file_size:.2f} MB")

    return "Data generation complete."