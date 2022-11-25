import random
from time import sleep

class Tabuleiro:
    ## propriedades
    tabuleiro = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

    jogadas = []

    rodada = 0

    ## métodos
    def jogada(self, jogador, coluna, linha):
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            return 'jogada fora de escopo'
            
        if jogador == 0:
            jogada = self.tabuleiro[linha][coluna]
            if jogada != ' ':
                return 'posição já jogada'
            else:
                self.tabuleiro[linha][coluna] = 'O'
                self.rodada += 1
                self.jogadas.append([jogador, coluna, linha])
                if jogador == 0:
                    nome = 'O'
                else:
                    nome = 'Computador'
                sleep(0.5)
                return f'Jogador {nome} jogou na posição {linha + 1},{coluna + 1}.'
        
        if jogador == 1:
            jogada = self.tabuleiro[linha][coluna]
            if jogada != ' ':
                return 'posição já jogada'
            else:
                self.tabuleiro[linha][coluna] = 'X'
                self.rodada += 1
                self.jogadas.append([jogador, coluna, linha])
                if jogador == 0:
                    nome = 'O'
                else:
                    nome = 'Computador'
                sleep(0.8)
                return f'Jogador {nome} jogou na posição {linha + 1},{coluna + 1}.'
    
    def verifica_ganho(self):
        ## horizontais
        if self.tabuleiro[0][0] != ' ' and self.tabuleiro[0][0] == self.tabuleiro[0][1] and self.tabuleiro[0][0] == self.tabuleiro[0][2]:
            return True, self.jogadas[-1]
        if self.tabuleiro[1][0] != ' ' and self.tabuleiro[1][0] == self.tabuleiro[1][1] and self.tabuleiro[1][0] == self.tabuleiro[1][2]:
            return True, self.jogadas[-1]
        if self.tabuleiro[2][0] != ' ' and self.tabuleiro[2][0] == self.tabuleiro[2][1] and self.tabuleiro[2][0] == self.tabuleiro[2][2]:
            return True, self.jogadas[-1]

        ## verticais
        if self.tabuleiro[0][0] != ' ' and self.tabuleiro[0][0] == self.tabuleiro[1][0] and self.tabuleiro[0][0] == self.tabuleiro[2][0]:
            return True, self.jogadas[-1]
        if self.tabuleiro[0][1] != ' ' and self.tabuleiro[0][1] == self.tabuleiro[1][1] and self.tabuleiro[1][1] == self.tabuleiro[2][1]:
            return True, self.jogadas[-1]
        if self.tabuleiro[0][2] != ' ' and self.tabuleiro[0][2] == self.tabuleiro[1][2] and self.tabuleiro[0][2] == self.tabuleiro[2][2]:
            return True, self.jogadas[-1]

        ## diagonais
        if self.tabuleiro[0][0] != ' ' and self.tabuleiro[0][0] == self.tabuleiro[1][1] and self.tabuleiro[0][0] == self.tabuleiro[2][2]:
            return True, self.jogadas[-1]
        if self.tabuleiro[0][2] != ' ' and self.tabuleiro[0][2] == self.tabuleiro[1][1] and self.tabuleiro[0][0] == self.tabuleiro[2][0]:
            return True, self.jogadas[-1]


        return False, None


    def retorna_rodada(self):
        return self.rodada

    def print_do_tabuleiro(self):
        tab_print = f"""
    1 | 2 | 3
  -———————————-
1 | {self.tabuleiro[0][0]} | {self.tabuleiro[0][1]} | {self.tabuleiro[0][2]} |
  |___|___|___|
2 | {self.tabuleiro[1][0]} | {self.tabuleiro[1][1]} | {self.tabuleiro[1][2]} |
  |___|___|___|
3 | {self.tabuleiro[2][0]} | {self.tabuleiro[2][1]} | {self.tabuleiro[2][2]} |
  |   |   |   |
  -———————————-
"""
        return tab_print

# JOGO

tab = Tabuleiro()

atual = 0

while True:
    if tab.retorna_rodada() >= 9:
        break
    
    ganho, ultimo = tab.verifica_ganho()

    if ganho == True:
        print(f'Jogador {ultimo[0]} ganhou!')
        break
    
    ## título
    titulo = 'JOGO DA VELHA'
    print('=-'*15)
    print(titulo.center(25))
    print('=-'*15)
    print(tab.print_do_tabuleiro())
    print('=-'*15)

    if atual == 0:    
        while True:
            linha = int(input('Qual linha deseja jogar? -> '))
            coluna = int(input('Qual coluna deseja jogar? -> '))
            rodada = tab.jogada(atual, coluna -1, linha -1)
            sleep(0.5)
            if rodada == 'jogada fora de escopo':
                continue
            if rodada == 'posição já jogada':
                continue

            break

    if atual == 1:
        while True:
            rodada = tab.jogada(atual, random.randint(0,2), random.randint(0,2))
            sleep(0.5)
            if rodada == 'jogada fora de escopo':
                continue
            if rodada == 'posição já jogada':
                continue
            
            break


    if tab.jogadas[-1][0] == 0:
        atual = 1
    else:
        atual = 0

    print(rodada)