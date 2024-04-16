import hashlib
import csv

#myText = "Teste do texto em teste"

#SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
#MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

#print("\"" +myText + "\" - " + SHA256 + " - " + MD5)

def calcular_hash_sha256(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

def calcular_hash_md5(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def verificar_hashes(arquivo_csv):
    with open(arquivo_csv, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for linha in reader:
            #frase = linha[0].strip('"')
            frase = linha[0].strip('"').replace(r'\,', ',').replace(r'\"', '"')

            hash_sha256_calculado = calcular_hash_sha256(frase)
            hash_md5_calculado = calcular_hash_md5(frase)
            
            hash_sha256_csv = linha[1]
            hash_md5_csv = linha[2]

            print( '\n' +frase + " hash256= " + hash_sha256_calculado + " hcsv = " + hash_sha256_csv + '\n')
            
            # Verifica se os hashes calculados correspondem aos hashes do arquivo
            resultado_sha256 = "OK" if hash_sha256_calculado == hash_sha256_csv else "Erro"
            resultado_md5 = "OK" if hash_md5_calculado == hash_md5_csv else "Erro"
            
            print(f"{frase} - SHA256: {resultado_sha256}, MD5: {resultado_md5} \n")

#arquivo_csv = 'referenciasCorretas.csv'
arquivo_csv = 'frases.csv'
verificar_hashes(arquivo_csv)
