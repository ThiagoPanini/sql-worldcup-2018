class Selecao():
    def __init__(self, nome, j, p):
        self.nome = nome
        self.jogos = j
        self.pontos = p

    def imprime(self, nome):
        print(f'Seleção: {nome}')

brasil = Selecao('Brasil', 0, 0)
russia = Selecao('Russia', 0, 0)

print(brasil.jogos)
print(russia.jogos)

brasil.jogos += 1
print(brasil.jogos)
print(russia.jogos)