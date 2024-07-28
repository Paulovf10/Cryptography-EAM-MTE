
# Cryptography EAM MTE

Este projeto contém implementações de criptografia para os métodos EAM (Encrypt-and-MAC) e MTE (MAC-then-Encrypt).

## Estrutura do Projeto

- `src/`: Contém os módulos principais `base_crypto.py`, `eam.py` e `mte.py`.
- `tests/`: Contém os testes unitários para os módulos.

## Como Usar

### Instalar Dependências

```sh
pip install -r requirements.txt
```

### Executar Testes

```sh
python -m unittest discover tests
```

## Exemplo de Uso

Veja os arquivos `eam.py` e `mte.py` para exemplos de como encriptar e decriptar mensagens usando os métodos EAM e MTE.
