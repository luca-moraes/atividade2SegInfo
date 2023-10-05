import hashlib

myText = 'Teste do texto em teste'

SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest(

print("\"" +myText + "\" - " + SHA256 + " - " + MD5)

