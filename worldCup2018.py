"""Projeto Copa do Mundo 2018 - Análise

Ideia principal: realizar um sorteio randômico de placares de acordo com o enfrentamento das seleções no decorrer
da Copa. As seleções serão divididas em 2 grupos: os favoritos e as zebras. O que define a chance de vitória de uma
seleção sobre a outra é o sorteio de placares em duas listas diferentes (favoritos e zebra), cada qual com resultados
possíveis de gols marcados por determinada seleção em cada partida"""

from time import sleep
from random import randint

favorito = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4]  # Lista favorito com gols possíveis de serem marcados por seleções favoritas
zebra = [0, 0, 0, 0, 1, 1, 1, 1, 2, 3]  # Lista zebra com gols possíveis de serem marcados por seleções zebra
status = {'Jogos': 0, 'Total de Gols': 0}

# Cadastrando todas as 32 seleções participantes
russia = {'Nome': 'Russia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
brasil = {'Nome': 'Brasil', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
ira = {'Nome': 'Irã', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
japao = {'Nome': 'Japão', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
mexico = {'Nome': 'México', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
belgica = {'Nome': 'Bélgica', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
coreia = {'Nome': 'Coréia do Sul', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
arabia = {'Nome': 'Arábia Saudita', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
alemanha = {'Nome': 'Alemanha', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
inglaterra = {'Nome': 'Inglaterra', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
espanha = {'Nome': 'Espanha', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
nigeria = {'Nome': 'Nigéria', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
costa = {'Nome': 'Costa Rica', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
polonia = {'Nome': 'Polônia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
egito = {'Nome': 'Egito', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
islandia = {'Nome': 'Islândia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
servia = {'Nome': 'Sérvia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
franca = {'Nome': 'França', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
portugal = {'Nome': 'Portugal', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
argentina = {'Nome': 'Argentina', 'Tipo': favorito, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
colombia = {'Nome': 'Colômbia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
uruguai = {'Nome': 'Uruguai', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
panama = {'Nome': 'Panamá', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
senegal = {'Nome': 'Senegal', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
marrocos = {'Nome': 'Marrocos', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
tunisia = {'Nome': 'Tunísia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
suica = {'Nome': 'Suiça', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
croacia = {'Nome': 'Croácia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
suecia = {'Nome': 'Suécia', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
dinamarca = {'Nome': 'Dinamarca', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
australia = {'Nome': 'Austrália', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}
peru = {'Nome': 'Peru', 'Tipo': zebra, 'J': 0, 'P': 0, 'V': 0, 'E': 0, 'D': 0, 'GP': 0, 'GC': 0, 'SG': 0}

# Separando as seleções em seus respectivos grupos (objeto)
class Grupo:
    A = [arabia, egito, russia, uruguai]
    B = [espanha, ira, marrocos, portugal]
    C = [australia, dinamarca, franca, peru]
    D = [argentina, croacia, islandia, nigeria]
    E = [brasil, costa, servia, suica]
    F = [alemanha, coreia, mexico, suecia]
    G = [belgica, inglaterra, panama, tunisia]
    H = [colombia, japao, polonia, senegal]

