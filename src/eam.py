from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from .base_crypto import BaseCrypto

class EAM(BaseCrypto):
    def __init__(self, chave):
        super().__init__(chave)

    def encriptar(self, mensagem):
        tag = self.generate_hmac(mensagem)
        cifra = AES.new(self.chave, AES.MODE_CBC)
        texto_cifrado = cifra.encrypt(self.padding(mensagem))
        return cifra.iv + texto_cifrado + tag

    def decriptar(self, cifrado):
        ivd = cifrado[:16]
        tagd = cifrado[-32:]
        cifra = AES.new(self.chave, AES.MODE_CBC, ivd)
        msge = cifra.decrypt(cifrado[16:-32])
        texto = self.dpadding(msge)
        if not self.verify_hmac(texto, tagd):
            return None
        return texto
