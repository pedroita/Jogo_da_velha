from Tabuleiro import Tabuleiro
from random import random
class Velha:
    def __init__(self) :
        self.__tabuleiro = Tabuleiro()
        if random()>=0.5:
            self.__jogador = 'X'
        else:
            self.__jogador = 'O'
    def imprime(self):
        print('\n' *50)
        print('Jogo da velha \n')
        self.__tabuleiro.imprime()
    def trocar_jogador(self):
        if self.__jogador == 'X':
            self.__jogador = 'O'
        else:
            self.__jogador = 'X'
    def pega_jogada(self):
        while True:
            self.imprime()
            print('\nJogador', self.__jogador)
            posicao = input('Informe a jogada: ')
            if self.__tabuleiro.jogada(posicao, self.__jogador):
                break
            else:
                print('Jogada inválida! Informe uma posição válida (ex: 1A).')
                input('Pressione Enter para continuar.')
        
    def eh_vencedor(self, jogador):
        linhas = self.__tabuleiro.todas_linhas()
        if tuple([jogador]*3) in linhas:
            return True
        return False
        

    def jogar (self):
        while self.__tabuleiro.tem_jogada():
            self.imprime()
            self.pega_jogada()
            if self.eh_vencedor(self.__jogador):
                self.imprime()
                print('\nFim de jogo!')
                print('Vitoria do jogador', self.__jogador)
                return
            self.trocar_jogador()
        self.imprime()
        print('\nJogo empatado!')