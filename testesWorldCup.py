"""Projeto Copa do Mundo 2018"""

"""Ideia principal: organizar um sorteio randomico de todos os confrontos da Copa do Mundo Russia 2018 a fim de 
decidir um campeão baseado em um único critério: favorito ou zebra."""

from time import sleep
from random import choice
from itertools import combinations

fav = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Quantidade de gols por partida a serem sorteados para o time Favorito
zebra = [0, 0, 0, 0, 1, 1, 1, 1, 2, 3]  # Quantidade de gols por partida a serem sorteados para times não-Favoritos
nomesGrupos = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G', 'Grupo H']


def cabecalhoRodada(n):
    """Imprime cabeçalho indicativo do número da RODADA"""
    print('-' * 35)
    print('{:^35}'.format('RODADA ' + str(n)))
    print('-' * 35)


def cabecalhoGrupo(texto):
    """Imprime cabeçalho indicativo do número da RODADA"""
    print('-' * 35)
    print('{:^35}'.format(texto))
    print('-' * 35)


def placar(time1, placar1, time2, placar2):
    """Imprime placar baseado no sorteio feito nas listas"""
    # print('-' * 35)
    print('{:>12}{:>4} x {:<4}{}'.format(time1, placar1, placar2, time2))
    # print('-' * 35)


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
        visitante.status['GC'] += golsHome  # Atualiza a quantidade de "Gols Contra" do time Visitante
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

    def organizaConfronto(self, grupos):
        for grupo in grupos:
            grupo = list(combinations(grupo, 2))

    def imprimeTabela(self, grupo):
        print('{}{}{}')



"""Instanciando todas as seleções"""

# Grupo A
arabia = Selecao('Arábia', False)
egito = Selecao('Egito', True)
russia = Selecao('Russia', False)
uruguai = Selecao('Uruguai', True)

grupoA = [arabia, egito, russia, uruguai]  # Objetos (seleções) do Grupo A guardados na lista grupoA

# Grupo B
espanha = Selecao('Espanha', True)
ira = Selecao('Irã', False)
marrocos = Selecao('Marrocos', False)
portugal = Selecao('Portugal', True)

grupoB = [espanha, ira, marrocos, portugal]  # Objetos (seleções) do Grupo B guardados na lista grupoB

# Grupo C
australia = Selecao('Austrália', False)
dinamarca = Selecao('Dinamarca', False)
franca = Selecao('França', True)
peru = Selecao('Peru', False)

grupoC = [australia, dinamarca, franca, peru]  # Objetos (seleções) do Grupo C guardados na lista grupoC

# Grupo D
argentina = Selecao('Argentina', True)
croacia = Selecao('Croácia', False)
islandia = Selecao('Islândia', False)
nigeria = Selecao('Nigéria', False)

grupoD = [argentina, croacia, islandia, nigeria]  # Objetos (seleções) do Grupo D guardados na lista grupoD

# Grupo E
brasil = Selecao('Brasil', True)
suica = Selecao('Suiça', False)
costa = Selecao('Costa Rica', False)
servia = Selecao('Sérvia', False)

grupoE = [brasil, suica, costa, servia]  # Objetos (seleções) do Grupo E guardados na lista grupoE

# Grupo F
alemanha = Selecao('Alemanha', True)
coreia = Selecao('Coreia', False)
mexico = Selecao('México', False)
suecia = Selecao('Suécia', False)

grupoF = [alemanha, coreia, mexico, suecia]  # Objetos (seleções) do Grupo F guardados na lista grupoF

# Grupo G
belgica = Selecao('Bélgica', True)
inglaterra = Selecao('Inglaterra', True)
panama = Selecao('Panamá', False)
tunisia = Selecao('Tunísia', False)

grupoG = [belgica, inglaterra, panama, tunisia]  # Objetos (seleções) do Grupo G guardados na lista grupoG

# Grupo H
colombia = Selecao('Colômbia', False)
japao = Selecao('Japão', False)
polonia = Selecao('Polônia', False)
senegal = Selecao('Senegal', False)

grupoH = [colombia, japao, polonia, senegal]  # Objetos (seleções) do Grupo H guardados na lista grupoH

"""Organizando confronto de seleções para que este nao se repita
Método combinations() transforma os objetos em cada grupo em tuplas com confrontos únicos"""
# As tentativas de automatizar o combinations() com um laço for e a lista geral copaMundo não surtiram efeito.
print(grupoA)
grupoA = list(combinations(grupoA, 2))
grupoB = list(combinations(grupoB, 2))
grupoC = list(combinations(grupoC, 2))
grupoD = list(combinations(grupoD, 2))
grupoE = list(combinations(grupoE, 2))
grupoF = list(combinations(grupoF, 2))
grupoG = list(combinations(grupoG, 2))
grupoH = list(combinations(grupoH, 2))

"""Organização geral dos grupos"""
copaMundo = [grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH]

print(copaMundo[0])

ordem = [(1, 0, 5), (2, 1, 4), (3, 2, 3)]

print(len(copaMundo[0]))

for rodada in ordem:
    cabecalhoRodada(rodada[0])
    for grupo in range(2):
        cabecalhoGrupo(nomesGrupos[grupo])
        Selecao.partida(Selecao, copaMundo[grupo][rodada[1]][0], copaMundo[grupo][rodada[1]][1])
        Selecao.partida(Selecao, copaMundo[grupo][rodada[2]][0], copaMundo[grupo][rodada[2]][1])






# for brasil. partida = lista com adversarios para ir percorrendo
# Cadastrar escalação de cada seleção e colocar quem fez o gol em cada partida e em qual minuto.
# Implementar GRUPOS e dividir partidas por RODADA no cabeçalho (RODADA 1 - GRUPO A - RESULTADOS)
# laço for para confrontos = se a seleção ja jogou 3 vezes, remove o nome da lista (pop ou del)
# Separar em RODADAS

# Ideia final: puxar dados do FIFA ou do PES e cadastrar cada jogador de cada seleção de acordo com os ratings.
# Determinar probabilidade de cada seleção ganhar determinada partida de acordo com um cálculo baseado no rating dos
# jogadores.
