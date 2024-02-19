from random import random
class Tabuleiro:
    def __init__(self) :
        self.__posicoes = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
        
    def imprime (self):
        print('\n |A|B|C')
        for cont, linha in enumerate (self.__posicoes):
            print ('------------')
            print(cont+1, '|' + '|'.join(linha), sep=' ')
    def jogada(self, posicao, simbolo):
        try:
            if len(posicao) < 2:
                raise ValueError

            linha = int(posicao[0]) - 1
            letra = posicao[1].upper()
            coluna = ord(letra) - ord('A')

            if self.__posicoes[linha][coluna] == ' ':
                self.__posicoes[linha][coluna] = simbolo
                return True
            else:
                print('Jogada inválida! A posição já está ocupada.')
                input('Pressione Enter para continuar.')

        except IndexError:
            print('Jogada inválida! A posição está fora do tabuleiro.')
            return False
    def tem_jogada(self):
        for linha in self.__posicoes:
            if ' ' in linha:
                return True
            else:
                print("posicao oculpada!")
        
    def todas_linhas(self):
        todas = []
        for linha in self.__posicoes:
            todas.append(tuple(linha))
        for cont in range(3):
            coluna = [self.__posicoes[0][cont],
                      self.__posicoes[1][cont],
                      self.__posicoes[2][cont]]
            todas.append(tuple(coluna))
        diagonal  = []
        transvesal = []
        for cont in range(3):
            diagonal.append(self.__posicoes[cont][cont])
            transvesal.append(self.__posicoes[2-cont][cont])
            todas.append(tuple(diagonal))
            todas.append(tuple(transvesal))
        return todas


