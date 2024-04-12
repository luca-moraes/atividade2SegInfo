import csv
import re

def processar_linha(linha):
    #linha = re.sub(r'\s*-\s*', '-', linha)
    #linha = linha.strip().replace('"', '')
    partes = linha.split(' - ')
    frase = partes[0]
    hashSHA256 = partes[1]
    hashMD5 = partes[2]
    return frase, hashSHA256, hashMD5

def converter_txt_para_csv(arquivo_txt, arquivo_csv):
    with open(arquivo_txt, 'r', encoding='utf-8') as txt_file, \
         open(arquivo_csv, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quotechar='', quoting=csv.QUOTE_NONE)
        writer = csv.writer(csv_file)
        # writer.writerow(['Frase', 'HashSHA256', 'HashMD5'])
        
        for linha in txt_file:
            if linha.strip():
                frase, hash1, hash2 = processar_linha(linha)
                writer.writerow([frase, hash1, hash2])

arquivo_entrada = 'frases.txt'
arquivo_saida = 'frases.csv'
converter_txt_para_csv(arquivo_entrada, arquivo_saida)
