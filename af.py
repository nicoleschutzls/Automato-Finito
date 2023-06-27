import math
import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

class AutomatoFinito:

    def __init__(self):
        self.estados = set()
        self.estado_inicial = None
        self.estados_finais = set()
        self.alfabeto = set()
        self.transicoes = {}

    def adicioneEstado(self, estado):
        self.estados.add(estado)

    def definineEstadoInicial(self, estado_inicial):
        if estado_inicial not in self.estados:
            print("O estado inicial informado não existe.")
            return False

        self.estado_inicial = estado_inicial
        return True

    def adicioneEstadoFinal(self, estado_final):
        if estado_final not in self.estados:
            print("O estado final informado não existe.")
            return False

        self.estados_finais.add(estado_final)
        return True

    def adicioneSimbolo(self, simbolo):
        self.alfabeto.add(simbolo)

    def adicioneTransicao(self, estado_origem, simbolo, estado_destino):
        if (estado_origem, simbolo) in self.transicoes:
            self.transicoes[(estado_origem, simbolo)].append(estado_destino)
        else:
            self.transicoes[(estado_origem, simbolo)] = [estado_destino]

    def validar(self):
        if self.estado_inicial is None:
            print("O estado inicial não foi definido.")
            return False

        if not self.estados_finais:
            print("Nenhum estado final foi definido. O autômato será finalizado.")
            return False

        for estado_origem, simbolo in self.transicoes.keys():
            if estado_origem not in self.estados or any(
                    estado_destino not in self.estados for estado_destino in self.transicoes[(estado_origem, simbolo)]):
                print("As transições referem-se a estados inexistentes.")
                return False

        return True

    def palavra(self, palavra):
        pilha_estados = [(self.estado_inicial, palavra)]

        while pilha_estados:
            estado_topo, palavra_restante = pilha_estados.pop()

            if not palavra_restante:
                if estado_topo in self.estados_finais:
                    return True

            else:
                simbolo = palavra_restante[0]
                palavra_restante = palavra_restante[1:]

                transicoes_possiveis = self.transicoes.get((estado_topo, simbolo), [])
                transicoes_vazias = self.transicoes.get((estado_topo, ''), [])

                for estado_destino in set(transicoes_possiveis).union(
                        transicoes_vazias):
                    pilha_estados.append((estado_destino, palavra_restante))

        return False

    def visualizar_grafo(self):
        G = nx.DiGraph()

        for estado in self.estados:
            G.add_node(estado)

        for estado_origem, simbolo in self.transicoes.keys():
            estados_destino = self.transicoes[(estado_origem, simbolo)]
            for estado_destino in estados_destino:
                label = str(simbolo)
                G.add_edge(str(estado_origem), str(estado_destino), label=label)

        num_estados = len(self.estados)
        raio = 2
        angulo_inicial = math.pi / 2
        angulo_incremento = 2 * math.pi / num_estados

        pos = {}

        for i, estado in enumerate(self.estados):
            angulo = angulo_inicial - i * angulo_incremento
            x = raio * math.cos(angulo)
            y = raio * math.sin(angulo)
            pos[estado] = (x, y)

        nx.draw_networkx(G, pos, with_labels=True, arrows=True)

        x, y = pos[self.estado_inicial]
        x_tri = x - 0.05
        y_tri = y

        triangle = Polygon([[x_tri, y_tri], [x_tri - 0.15, y_tri + 0.15],
                            [x_tri - 0.15, y_tri - 0.15]],
                           closed=True,
                           linewidth=1.0)
        plt.gca().add_patch(triangle)

        nx.draw_networkx_nodes(G,
                               pos,
                               nodelist=[self.estado_inicial],
                               node_shape='o')

        for estado in self.estados_finais:
            nx.draw_networkx_nodes(G,
                                   pos,
                                   nodelist=[estado],
                                   node_shape='o',
                                   node_size=500,
                                   edgecolors='black',
                                   linewidths=1.0)

        edge_labels = nx.get_edge_attributes(G, 'label')
        for edge, label in edge_labels.items():
            x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2
            y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2
            if label == '-':
                plt.text(x + 0.5, y, label, fontsize=6, horizontalalignment='center')
            else:
                plt.text(x - 0.1,
                         y + 0.3,
                         label,
                         fontsize=6,
                         horizontalalignment='center')

        plt.show()

def execute_afd():
    afd = AutomatoFinito()

    alfabeto = input("Digite os caracteres do alfabeto separados por vírgula: ").split(',')
    for simbolo in alfabeto:
        afd.adicioneSimbolo(simbolo)

    estados = input("Digite os estados separados por vírgula: ").split(',')
    for estado in estados:
        afd.adicioneEstado(estado)

    estado_inicial = input("Digite o estado inicial: ")
    while not afd.definineEstadoInicial(estado_inicial):
        estado_inicial = input("Digite um estado inicial válido: ")

    estado_final = input("Digite o estado final: ").split(',')
    while not all(afd.adicioneEstadoFinal(estado.strip()) for estado in estado_final):
        estado_final = input("Digite o estado final: ").split(',')

    print("Informe as transições de estados e caso queira encerrar a entrada de transições, digite 'fim': ")

    while True:
        entrada = input("> ")

        if entrada.lower() == 'fim':
            break

        transicao = entrada.split(',')
        if len(transicao) != 3:
            print("Entrada inválida.")
            continue

        estado_origem, simbolo, estado_destino = map(str.strip, transicao)

        afd.adicioneTransicao(estado_origem.lower(), simbolo, estado_destino.lower())

    palavra = input("Digite uma palavra ou 'sair' para encerrar: ")
    while palavra.lower() != 'sair':
        if afd.palavra(palavra):
            print(f"A palavra '{palavra}' é aceita pelo autômato.")
        else:
            print(f"A palavra '{palavra}' é rejeitada pelo autômato.")

        palavra = input("Digite uma palavra ou 'sair' para encerrar: ")

    afd.visualizar_grafo()

execute_afd()
