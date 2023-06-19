from unidecode import unidecode
import platform,os
from time import sleep

#Dicionário pra colorir o console
ANSI = {
"GREEN" : "\033[0;32m" ,
"RED" : "\033[1;31m",
"RESET" : "\033[0;0m",
"BLUE" : "\033[1;34m"
}

#Histórico dos jogadores
historico = [[],[]]

#Limpa o console
def limparConsole():
  if platform.system() == "Windows":
    os.system("cls")
  elif platform.system() == "Linux":
    os.system("clear")

#Menu inicial
def show_menu():
  print(ANSI["BLUE"])
  print("----------------")
  print("      Termo     ")
  print("                ")
  print("Desenvolvido por")
  print("     Ivan Jr    ")
  print("----------------")
  print(ANSI["RESET"],end="\n")

#Verificação das letras
def verificar(resp,plvr):

  if len(plvr) != 5:
    print("Palavra diferente do esperado!")
    return "Erro de tamanho"
  if plvr == resp:
    print(ANSI['GREEN'] + plvr + ANSI['RESET'])
    return True

  retorno = []
  
  for i in range(5):

    #Verifica se é verde(Posição certa)
    if plvr[i] == resp[i]:
      retorno.append(f"{ANSI['GREEN']}{plvr[i]}{ANSI['RESET']}")
      if (f"{ANSI['RED']}{plvr[i]}") in retorno:
        indice = retorno.index(f"{ANSI['RED']}{plvr[i]}{ANSI['RESET']}")
        retorno[indice] = plvr[i]
      
    #Verifica se é vermelha(Posição errada)
    elif plvr[i] in resp and retorno.count(plvr[i]) < resp.count(plvr[i]):
      retorno.append(f"{ANSI['RED']}{plvr[i]}{ANSI['RESET']}")
    #Deixa sem cor(Não existe na palavra)
    else:
      retorno.append(f"{ANSI['RESET']}{plvr[i]}")

  for i in range(5):
    plvrNaPosicaoErrada = f"{ANSI['RED']}{plvr[i]}{ANSI['RESET']}"
    plvrNaPosicaoCerta = f"{ANSI['GREEN']}{plvr[i]}{ANSI['RESET']}"
    qntdJaExistente =  retorno.count(plvrNaPosicaoErrada) + retorno.count(plvrNaPosicaoCerta)
    if qntdJaExistente > resp.count(plvr[i]):
      if retorno[i] == f"{ANSI['RED']}{plvr[i]}{ANSI['RESET']}":
        retorno[i] = plvr[i]
  
  return retorno

#Organizar palavras numa lista
def orgPalavras():
  # texto = input("Texto: ")
  texto = input("Texto> ")
  texto = unidecode(texto.lower()) #Texto para minúsculo e sem acentos

  #Remover caracteres especiais
  caracteres = "?!,.:;_-@"
  for i in range(len(caracteres)):  
    texto = texto.replace(caracteres[i],"") 
  
  palavras = texto.split()
  
  listaPlvrs= [palavra for palavra in palavras if len(palavra) == 5]
  
  #Remover palavras repitidas
  remover = []
  for i in range(len(listaPlvrs)):
    if listaPlvrs.count(listaPlvrs[i]) > 1:
      remover.append(listaPlvrs[i])

  for palavra in remover:
    index = listaPlvrs.index(palavra)
    if listaPlvrs.count(palavra) > 1:
      listaPlvrs.remove(listaPlvrs[index])
  
  return listaPlvrs

def qntdRodadas():
  while True:
    rodadas = int(input("Quantidade de Rodadas: "))
    if rodadas % 2 != 0:
        print("[Quantidade Inválida] Digite um número PAR de rodadas")
    else:
        return rodadas

#Função de rodadas
def rodada(plvr,nomeJogador,nJogador):
  print(f"Vez de {nomeJogador}")
  pontos = 120
  situacao = "N encontrou"
  mostrarHistorico(historico[nJogador])
  while pontos > 0:
    palpite = input('>') 
    resultado = (verificar(plvr,palpite))
    if resultado == True:
      situacao = "Encontrou"
      historico[nJogador].append((situacao,pontos))
      sleep(4)
      break
    elif resultado != "Erro de tamanho":
      print(*resultado)
      pontos -= 20
    
    if pontos == 0:
        historico[nJogador].append((situacao,pontos))

  if pontos == 0:
    print("[ACABOU AS CHANCES!] Fim da rodada")
    sleep(3)
  limparConsole()

#somar pontos de todas as partidas
def somarPontos(historico):
  pontos = 0
  for i in range(len(historico)):
    pontoRodada = historico[i][1]
    pontos += pontoRodada
  return pontos


#Mostrar o historico
def mostrarHistorico(historico):
  print("Histórico do Jogador:\n")
  for i in range(len(historico)):
    print(f"|Rodada {i}: Situação({historico[i][0]}) Pts({historico[i][1]})",end='|\n')

def finalizar(p1,p2):
  pontos1 = somarPontos(historico[0])
  pontos2 = somarPontos(historico[1])

  print("       Fim do Jogo     ")
  print("<--------------------->")
  print(f"{p1}: {pontos1} pontos")
  print(f"{p2}: {pontos2} pontos")
  print("<--------------------->")
  
  if pontos1 > pontos2:
    print(f"Jogador vencedor: {p1}, com total de {pontos1} pontos.")
  elif pontos2 > pontos1:
    print(f"Jogador vencedor: {p2}, com total de {pontos2} pontos.")
  else:
    print(f"Houve empate de pontos: {p1} para os dois jogadores")