import funcoes as fnc
import random

PALAVRAS = fnc.orgPalavras()
RODADAS = fnc.qntdRodadas()

jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")

fnc.limparConsole()

for i in range(RODADAS):
  fnc.show_menu()
  palavra = random.choice(PALAVRAS)
  jogadores = [jogador1,jogador2]
  if i % 2 == 0:
    jogadorDaVez = 0
  else:
    jogadorDaVez = 1
  
  fnc.rodada(palavra,jogadores[jogadorDaVez],jogadorDaVez)

fnc.finalizar(jogador1,jogador2)