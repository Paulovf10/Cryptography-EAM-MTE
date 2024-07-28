import unittest
from src.eam import EAM
from Crypto.Random import get_random_bytes

class TestEAM(unittest.TestCase):
    def test_encriptar_decriptar(self):
        mensagem = b"Teste de mensagem"
        chave = get_random_bytes(16)
        eam = EAM(chave)
        cifrado = eam.encriptar(mensagem)
        decifrado = eam.decriptar(cifrado)
        self.assertEqual(mensagem, decifrado)

if __name__ == "__main__":
    unittest.main()
