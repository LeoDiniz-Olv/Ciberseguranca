import os
import pyaes

##Abrindo arquivo criptografado

nome_arquivo = 'teste.txt.ransomwaretroll'
arquivo = open(nome_arquivo, 'rb')
dados_arquivo = arquivo.read()
arquivo.close()

##Chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
dados_decriptados = aes.decrypt(dados_arquivo)

##Remover o arquivo criptografado

os.remove(nome_arquivo)

##Criando o arquivo descriptografado

novo_arquivo  = 'teste.txt'
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(dados_decriptados)
novo_arquivo.close()

