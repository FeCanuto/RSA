import threading
from diffie_hellman import dh_client
import rsa

while True:

    p = dh_client()
    q = dh_client()
    value = dh_client()

    if p != q :
        print(f"p = {p}")
        print(f"q = {q}")
        print(f"value = {value}")
        break

text = input("Inserir Mensagem: ")

n = p*q  # compute N
y = rsa.totient(p)  # computa o totient de P
x = rsa.totient(q)  # computa o totient de Q
totient_de_N = x*y  # computa o totient de N
e = rsa.co_primo(totient_de_N, value)  # generate E
public_key = (n, e) # Chave pública 
text_cipher = rsa.cipher(text, e, n) # Criptografa Mensagem
d = rsa.calculando_chave_privada(totient_de_N, e) # Chave Privada
original_text = rsa.descifra(text_cipher, n, d)  # Descriptografa Mensagem

# Exibir informações sobre as chaves e texto cifrado/decifrado 
print('|Chave Pública          >> ', public_key)
print('|Mensagem criptografada >> ', text_cipher)
print('|Chave Privada          >> ', d)
print('|Mensagem Original      >> ', original_text)
