"""Projeto Copa do Mundo 2018"""

"""Ideia principal: organizar um sorteio randomico de todos os confrontos da Copa do Mundo Russia 2018 a fim de 
decidir um campeão baseado em um único critério: favorito ou zebra."""

from time import sleep
from random import choice

fav = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Quantidade de gols por partida a serem sorteados para o time Favorito
zebra = [0, 0, 0, 0, 1, 1, 1, 1, 2, 3]  # Quantidade de gols por partida a serem sorteados para times não-Favoritos


def placar(time1, placar1, time2, placar2):
    """Imprime placar baseado no sorteio feito nas listas"""
    print('-' * 35)
    print('{:>12}{:>4} x {:<4}{}'.format(time1, placar1, placar2, time2))
    print('-' * 35)


class Selecao():
    def __init__(self, nome, favorito):
        """Método construtor"""
        """Atributos: Nome, Favorito, Status"""
        self.nome = nome
        self.favorito = favorito
        self.status = {'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
        self.ranking = 1

    def partida(self, casa, visitante):
        """Recebe duas seleções e organiza uma partida entre elas
        Define também os parâmetros a serem atualizados no "Status" geral de cada seleção."""

        if casa.favorito:  # Se o time da "Casa" é favorito, escolha os gols na lista de favoritos (maior chance)
            golsHome = choice(fav)
        else:  # Caso contrário, escolha os gols do time da "Casa" na lista de zebra (menor chance)
            golsHome = choice(zebra)
        if visitante.favorito:  # Se o "Visitante" é favorito, escolha os gols na lista de favoritos (maior chance)
            golsVisit = choice(fav)
        else:  # Caso contrário, escolha os gols do "Visitante" na lista de zebra (menor chance)
            golsVisit = choice(zebra)

        placar(casa.nome, golsHome, visitante.nome, golsVisit)

        casa.status['J'] += 1  # Atualiza quantidade de "Jogos" do time da Casa
        casa.status['GP'] += golsHome  # Atualiza a quantidade de "Gols Pro" do time da Casa
        casa.status['GC'] += golsVisit  # Atualiza a quantidade de "Gols Contra" do time da Casa
        casa.status['SG'] = casa.status['GP'] - casa.status['GC']  # Atualiza "Saldo de Gols" do time da Casa
        visitante.status['J'] += 1  # Atualiza a quantidade de "Jogos" do time Visitante
        visitante.status['GP'] += golsVisit  # Atualiza a quantiade de "Gols Pro" do time Visitante
        visitante.status['GC'] += golsVisit  # Atualiza a quantidade de "Gols Contra" do time Visitante
        visitante.status['SG'] = visitante.status['GP'] - visitante.status['GC']  # "Saldo de Gols" do Visitante

        if golsHome > golsVisit:  # Caso o time da "Casa" vença, atualiza "Vitórias" e "Pontos" (+3)
            casa.status['V'] += 1
            casa.status['P'] += 3
        elif golsHome == golsVisit:  # Caso dê empate, atualize "Empate" e "Pontos" (+1) de ambas as seleções
            casa.status['E'] += 1
            visitante.status['E'] += 1
            casa.status['P'] += 1
            visitante.status['P'] += 1
        else:  # Caso contrário (time Visitante vença), atualize "Vitórias" e "Pontos" (+3) do time Visitante
            visitante.status['V'] += 1
            visitante.status['P'] += 3

    def imprimeTabela(self):
        pass


"""Instanciando todas as seleções"""

# Grupo A
arabia = Selecao('Arábia', False)
egito = Selecao('Egito', True)
russia = Selecao('Russia', False)
uruguai = Selecao('Uruguai', True)

grupoA = [arabia, egito, russia, uruguai]

# Grupo B
espanha = Selecao('Espanha', True)
ira = Selecao('Irã', False)
marrocos = Selecao('Marrocos', False)
portugual = Selecao('Portugal', True)

grupoB = [espanha, ira, marrocos, portugual]

# Grupo C
australia = Selecao('Austrália', False)
dinamarca = Selecao('Dinamarca', False)
franca = Selecao('França', True)
peru = Selecao('Peru', False)

grupoC = [australia, dinamarca, franca, peru]

# Grupo D
argentina = Selecao('Argentina', True)
croacia = Selecao('Croácia', False)
islandia = Selecao('Islândia', False)
nigeria = Selecao('Nigéria', False)

grupoD = [argentina, croacia, islandia, nigeria]

# Grupo E
brasil = Selecao('Brasil', True)
suica = Selecao('Suiça', False)
costa = Selecao('Costa Rica', False)
servia = Selecao('Sérvia', False)

grupoE = [brasil, suica, costa, servia]

# Grupo F
alemanha = Selecao('Alemanha', True)
coreia = Selecao('Coreia', False)
mexico = Selecao('México', False)
suecia = Selecao('Suécia', False)

grupoF = [alemanha, coreia, mexico, suecia]

# Grupo G
belgica = Selecao('Bélgica', True)
inglaterra = Selecao('Inglaterra', True)
panama = Selecao('Panamá', False)
tunisia = Selecao('Tunísia', False)

grupoG = [belgica, inglaterra, panama, tunisia]

# Grupo H
colombia = Selecao('Colômbia', False)
japao = Selecao('Japão', False)
polonia = Selecao('Polônia', False)
senegal = Selecao('Senegal', False)

grupoH = [colombia, japao, polonia, senegal]

for selecao in grupoA:
    print(selecao.nome)
    print(selecao.status)

# for brasil. partida = lista com adversarios para ir percorrendo
# Cadastrar escalação de cada seleção e colocar quem fez o gol em cada partida e em qual minuto.
# Implementar GRUPOS e dividir partidas por RODADA no cabeçalho (RODADA 1 - GRUPO A - RESULTADOS)
# laço for para confrontos = se a seleção ja jogou 3 vezes, remove o nome da lista (pop ou del)
# Separar em RODADAS

# Ideia final: puxar dados do FIFA ou do PES e cadastrar cada jogador de cada seleção de acordo com os ratings.
# Determinar probabilidade de cada seleção ganhar determinada partida de acordo com um cálculo baseado no rating dos
# jogadores.
