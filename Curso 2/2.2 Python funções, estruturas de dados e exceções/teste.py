# ##### 6 ######

# #. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

# # maior nota
# # menor nota
# # média
# # situação (Aprovado(a) ou Reprovado(a))

# #"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"


# from random import random

# def gerador_nota():
#     notas = []

#     for i in range(4):
#         notas.append(round(random() * 10, 2))
    
#     return notas

# notas = gerador_nota()
# maior_nota = max(notas)
# menor_nota = min(notas)
# media = round(sum(notas) / len(notas), 2)
# situacao = 'Aprovado' if media >= 6 else 'Reprovado'

# print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}')




# ########## 7 ###########

# # Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# for i in range(len(nomes)):
#     print(f'{nomes[i].capitalize()} {sobrenomes[i].capitalize()}')

# ########## 8 ###########
# #  Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

# # Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]

# def calcula_pontos(marcados, sofridos):
#     pontos = 0

#     for i in range(len(gols_marcados)):
#         if gols_marcados[i] > gols_sofridos[i]:
#             pontos += 3
#         elif gols_marcados[i] == gols_sofridos:
#             pontos += 1
    
#     return pontos

# pontos = calcula_pontos(gols_marcados, gols_sofridos)

# aproveitamento = pontos / (len(gols_sofridos) * 3) * 100

# print(f'A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento}%')

# #"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
 


########## 9 ############
# Você recebeu o desafio de criar um có digo que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

gasto_hotel = lambda dias: dias * 150
gasto_gasolina = lambda distancia, consumo, preco: (distancia / consumo) * preco

def gasto_passeio(cidade, dias):
    if cidade == 'Salvador':
        return 200 * dias
    elif cidade == 'Fortaleza':
        return 400 * dias
    elif cidade == 'Natal':
        return 250 * dias
    elif cidade == 'Aracaju':
        return 300 * dias

print(f'''Viagem de 3 dias de Salvador -> Recife
    Gasto de hotel: {gasto_hotel(3)}
    Gasto de gasolina: {gasto_gasolina(850*2, 14, 5)}
    Gasto passeio e alimentação: {gasto_passeio('Salvador', 3)}
      ''')
