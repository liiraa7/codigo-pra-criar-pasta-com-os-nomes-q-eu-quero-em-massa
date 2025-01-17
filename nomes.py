import os

# Caminho do diretório de origem
origem = "i:\\"

if os.path.exists(origem):
    pastas = [nome for nome in os.listdir(origem) if os.path.isdir(os.path.join(origem, nome))]
    print(pastas)
else:
    print(f"O caminho '{origem}' não foi encontrado.")
    
# Obtém a lista de pastas no diretório de origem
pastas = [nome for nome in os.listdir(origem) if os.path.isdir(os.path.join(origem, nome))]

# Exibe os nomes das pastas
for pasta in pastas:
    print(pasta)

# Caso queira salvar os nomes das pastas em um arquivo de texto:
with open('nomes_das_pastas.txt', 'w') as f:
    for pasta in pastas:
        f.write(pasta + '\n')

print("Nomes das pastas salvos em 'nomes_das_pastas.txt")
1