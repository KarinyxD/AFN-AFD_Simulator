##### Simula um AFD ou AFN com base em uma tabela de transição 
##### e verifica se uma palavra é aceita pelo autômato ou não
##### Caio Augusto Reis e Kariny M. P. Abrahão - Disciplina: Teoria de Linguagens

from automato import Automato
import pandas as pd 

def main():
    automato = Automato()
    #Do-While(executa pelo menos uma vez)
    while True:
        automato.simular_automato()
        automato.verifica_estado()

        # Condição de saída do loop
        resposta = input("Deseja testar outra entrada? (s/n): ")
        if resposta.lower() != "s":
            break
        else:
            automato.setEntrada()

############
main()

