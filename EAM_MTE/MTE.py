from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome.Hash import HMAC
from Cryptodome.Random import get_random_bytes

# MTE


def padding(mensagem):  # Funcao de padding
    mensagem = mensagem + b'\x01'  # Coloca o byte no final da msg \x01
    while len(mensagem) % 16 != 0:  # Enquanto o tamanho da mensagem nao for mltiplo de 16
        mensagem = mensagem + b'\x00'  # Prenche o resto da mensagem com \x00
    return mensagem  # Retorna a mensagem apos o padding


def dpadding(mensagem):  # Funcao de dpadding
    cont = mensagem.count(b'\x00')  # Conta quantis \x00 tem na mensagem
    final_str = mensagem[:-cont]  # Remove os \x00 da mensagem
    final = final_str[:-1]  # Remove o \x01 da mensagem
    return final  # Retorna ela sem o padding


def mte_encriptar(mensagem, chave):
    hmac = HMAC.new(chave, mensagem, SHA256)  # Mac produzido a partir da mensagem
    tag = hmac.digest()  # Faz a tag
    cifra = AES.new(chave, AES.MODE_CBC)  # Escolhe o modo de operacao
    msg_pad = padding(mensagem)  # Faz o padding da mensagem
    texto_mac = msg_pad + tag  # Concatena a mensagem com a tag
    texto_cifrado = cifra.encrypt(texto_mac)  # Encripta a concatenacao entre a mensagem e a tag
    return cifra.IV + texto_cifrado  # Retorna a mensagem encriptada


def mte_decriptar(cifrado, chave):
    ivd = cifrado[:16]  # ivd recebe o iv da mensagem encriptada
    cifra = AES.new(chave, AES.MODE_CBC, ivd)  # Seleciona o modo de operacao
    msge = cifra.decrypt(cifrado)  # Decripta a mensagem
    tagd = msge[-32:]  # A partir da mensagem decriptada pega a tag
    texto_cifradod = msge[16: -32]  # A partir da mensagem decriptada pega mensagem inicial
    texto = dpadding(texto_cifradod)  # Faz o dpadding
    hmac = HMAC.new(chave, texto, SHA256)  # Faz o mac a partir da mensagem inicial
    try:  # Faz a verificacao do mac
        hmac.verify(tagd)
    except ValueError:
        print("Verificavao da tag falho.")
        return

    return texto


a = input("Digite a mensagem: ")  # Recebe a mensagem
msg = str.encode(a)  # Transforma em bytes
key = get_random_bytes(16)  # Gera a chave
c = mte_encriptar(msg, key)  # Encripta a mensagem
iv = c[:16]  # Gera o iv
tg = c[-32:]  # Gera a tag
texto_cif = c[16: -32]  # Gera o texto cifrado
print("Apos a encriptacao: ", c)  # Printa a mensagem encriptada
print("IV: ", iv)  # Printa o IV
print("Mensagem: ", texto_cif)  # Printa o texto cifrado
print("Tag: ", tg)  # Printa a tag
msgdecri = mte_decriptar(c, key)  # Desemcripta a mensagem
print("Mensagem decriptada: ", msgdecri)  # Printa a mensagem decriptada

