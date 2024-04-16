import csv
import re

def processar_linha(linha):
    linha = re.sub(r'\r?\n', ' ', linha.strip())
    match = re.match(r'"(.*?)" - ([a-f0-9]{64}) - ([a-f0-9]{32})', linha)
    if not match:
        raise ValueError("Linha mal formatada ou problema na divisão dos campos")
    frase = '"' + match.group(1) + '"'
    hashSHA256 = match.group(2)
    hashMD5 = match.group(3)
    return frase, hashSHA256, hashMD5

def converter_txt_para_csv(arquivo_txt, arquivo_csv):
    with open(arquivo_txt, 'r', encoding='utf-8') as txt_file, \
         open(arquivo_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quotechar='', quoting=csv.QUOTE_NONE, escapechar='\\')
        # writer = csv.writer(csv_file)
        # writer.writerow(['Frase', 'HashSHA256', 'HashMD5'])
        
        for linha in txt_file:
            if linha.strip():
                frase, hash1, hash2 = processar_linha(linha)
                writer.writerow([frase, hash1, hash2])

arquivo_entrada = 'frases.txt'
arquivo_saida = 'frases.csv'

# arquivo_entrada = 'referenciasCorretas.txt'
# arquivo_saida = 'referenciasCorretas.csv'

converter_txt_para_csv(arquivo_entrada, arquivo_saida)
