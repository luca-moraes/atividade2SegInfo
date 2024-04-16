import hashlib
import csv
from colorama import init, Fore, Style

init(autoreset=True)

#myText = "Teste do texto em teste"

#SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
#MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

#print("\"" +myText + "\" - " + SHA256 + " - " + MD5)

def calcular_hash_sha256(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

def calcular_hash_md5(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def hash_colorido(hash_fornecido, hash_calculado):
    if hash_calculado == hash_fornecido:
        return f"{Fore.GREEN}{hash_fornecido}{Style.RESET_ALL}"
    else:
        #pinta de vermelho o errado
        resultado_formatado = []
        for char_forn, char_calc in zip(hash_fornecido, hash_calculado):
            if char_calc == char_forn:
                resultado_formatado.append(f"{Fore.BLUE}{char_forn}{Style.RESET_ALL}")
            else:
                resultado_formatado.append(f"{Fore.RED}{char_forn}{Style.RESET_ALL}")
        return ''.join(resultado_formatado)

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
            
            #verificando os hashes
            if hash_sha256_calculado == hash_sha256_csv:
                resultado_sha256 = f"{Fore.GREEN}OK{Style.RESET_ALL}"
            else:
                resultado_sha256 = f"{Fore.RED}Erro{Style.RESET_ALL}"

            if hash_md5_calculado == hash_md5_csv:
                resultado_md5 = f"{Fore.GREEN}OK{Style.RESET_ALL}"
            else:
                resultado_md5 = f"{Fore.RED}Erro{Style.RESET_ALL}"
            
            print(f"{frase} - SHA256: {resultado_sha256}; MD5: {resultado_md5} \n")
            print("SHA256 calculado: "+f"{Fore.GREEN}{hash_sha256_calculado}{Style.RESET_ALL}"+"\nSHA256 fornecido: " + hash_colorido(hash_sha256_csv, hash_sha256_calculado) + '\n')
            print("MD5 calculado: "+f"{Fore.GREEN}{hash_md5_calculado}{Style.RESET_ALL}"+"\nMD5 fornecido: " + hash_colorido(hash_md5_csv, hash_md5_calculado) + '\n')

#arquivo_csv = 'referenciasCorretas.csv'
arquivo_csv = 'frases.csv'
verificar_hashes(arquivo_csv)
