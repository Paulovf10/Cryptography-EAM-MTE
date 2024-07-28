from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC

class BaseCrypto:
    def __init__(self, chave):
        self.chave = chave

    def padding(self, mensagem):
        mensagem = mensagem + b'\x01'
        while len(mensagem) % 16 != 0:
            mensagem = mensagem + b'\x00'
        return mensagem

    def dpadding(self, mensagem):
        cont = mensagem.count(b'\x00')
        final_str = mensagem[:-cont]
        final = final_str[:-1]
        return final

    def generate_hmac(self, mensagem):
        hmac = HMAC.new(self.chave, mensagem, SHA256)
        return hmac.digest()

    def verify_hmac(self, mensagem, tag):
        hmac = HMAC.new(self.chave, mensagem, SHA256)
        try:
            hmac.verify(tag)
        except ValueError:
            print("Verificação da tag falhou.")
            return False
        return True
