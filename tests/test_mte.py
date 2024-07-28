import unittest
from src.mte import MTE
from Crypto.Random import get_random_bytes

class TestMTE(unittest.TestCase):
    def test_encriptar_decriptar(self):
        mensagem = b"Teste de mensagem"
        chave = get_random_bytes(16)
        mte = MTE(chave)
        cifrado = mte.encriptar(mensagem)
        decifrado = mte.decriptar(cifrado)
        self.assertEqual(mensagem, decifrado)

if __name__ == "__main__":
    unittest.main()
