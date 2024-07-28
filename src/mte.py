from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from .base_crypto import BaseCrypto

class MTE(BaseCrypto):
    def __init__(self, chave):
        super().__init__(chave)

    def encriptar(self, mensagem):
        tag = self.generate_hmac(mensagem)
        cifra = AES.new(self.chave, AES.MODE_CBC)
        msg_pad = self.padding(mensagem)
        texto_mac = msg_pad + tag
        texto_cifrado = cifra.encrypt(texto_mac)
        return cifra.iv + texto_cifrado

    def decriptar(self, cifrado):
        ivd = cifrado[:16]
        cifra = AES.new(self.chave, AES.MODE_CBC, ivd)
        msge = cifra.decrypt(cifrado[16:])
        tagd = msge[-32:]
        texto_cifradod = msge[:-32]
        texto = self.dpadding(texto_cifradod)
        if not self.verify_hmac(texto, tagd):
            return None
        return texto
