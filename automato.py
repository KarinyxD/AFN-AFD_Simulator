import pandas as pd
class Automato:
    ##Construtor do objeto, inicia solicitando o arquivo da tabela, estados finais e a entrada
    def __init__(self):
        self.setTabela()
        self.setEstadoInicial()
        self.setEstadosFinais()
        self.setEntrada()
        self.estado_atual = None

    ##solicita o arquivo CSV, que contém a tabela de transições
    def setTabela(self):
        #Carregar tabela de transição de estados do arquivo CSV
        nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ")
        self.tabela = pd.read_csv(nome_arquivo)
        print(self.tabela)

    ##solicita o estado inicial
    def setEstadoInicial(self):
        self.estado_inicial = input("Digite o estado inicial: ")

    ##solicita o(s) estado(s) final(s) e transforma em uma lista
    def setEstadosFinais(self):
        self.estados_finais = input("Digite o(s) estado(s) final(s), separando-o(s) por vírgula: ")
        self.estados_finais = self.estados_finais.split(',') #separa os estados em uma lista

    ##solicita a entrada à ser testada pelo autômato
    def setEntrada(self):
        self.entrada = input("Digite a entrada que deseja testar: ")
        self.entrada = list(self.entrada) #transforma a string em uma lista

    ##metodo para simular o autômato com base na entrada fornecida e armazena o ultimo estado na variavel 'estado_atual'
    def simular_automato(self):
        #procura na primeira coluna a linha que possui o estado inicial
        linha_estado_atual = self.tabela[self.tabela.iloc[:, 0] == self.estado_inicial]
        #recebe o estado resultante da primeira transição
        self.estado_atual = linha_estado_atual[self.entrada[0]].iloc[0]
        #separa os estados em uma lista
        self.estado_atual = self.estado_atual.split(',')

        #loop para verificar cada simbolo da entrada(a partir do segundo elemento)
        for simbolo in self.entrada[1:]:
            conj_estado = ''
            #loop para percorrer os elementos da lista
            for estado in self.estado_atual:
                #essa variavel recebe a linha que contem um dos estados do conjunto de estados
                linha_estado_atual = self.tabela[self.tabela.iloc[:,0].str.contains(estado, na=False)]
                if not linha_estado_atual[simbolo].empty: #verifica se o conteúdo não está vazio
                    #une os estados resultantes após a transição
                    conj_estado += linha_estado_atual[simbolo].iloc[0] + ","
            self.estado_atual = conj_estado
            self.estado_atual = self.estado_atual.split(',') #separa os estados em uma lista
            self.estado_atual = list(filter(None,self.estado_atual)) #remove elementos nulos
            self.estado_atual = list(set(self.estado_atual)) #remove repetições
        return self.estado_atual #retorna o ultimo estado
   
    ##metodo para verificar se o estado em que terminou a palavra é um estado final
    def verifica_estado(self):
        #Forma 2 cojuntos a partir das listas e o '&' verifica se há interseção entre eles
        verifica = bool(set(self.estado_atual) & set(self.estados_finais)) #bool faz retornar True ou False
        if verifica == True: 
            print("A palavra '"+''.join(self.entrada)+ "' é aceita pelo autômato.")
        else: 
            print("A palavra '"+''.join(self.entrada)+"' não é aceita pelo autômato.")

