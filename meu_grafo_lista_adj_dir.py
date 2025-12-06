from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        pass # Apague essa instrução e inicie seu código aqui

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau_entrada(self, V=''):
        '''
        Provê o grau de entrada do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau de saída do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V in [v.rotulo for v in self.vertices]:
            return {a for a in self.arestas if V in (self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo)}
        raise VerticeInvalidoError

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def dijkstra(self, origem, destino):
        # Vértices válidos
        if origem not in (l := [v.rotulo for v in self.vertices]) or destino not in l:
            raise VerticeInvalidoError

        P = {v.rotulo: float('inf') for v in self.vertices}
        A = {v.rotulo: None for v in self.vertices}
        V = set()

        P[origem] = 0

        while len(V) < len(self.vertices):
            vertice = min((v.rotulo for v in self.vertices if v.rotulo not in V),
                          key=lambda rot: P[rot])

            if P[vertice] == float('inf'):
                break

            V.add(vertice)

            for a in self.arestas_sobre_vertice(vertice):
                if int(self.arestas[a].peso) < 0:
                    raise ArestaInvalidaError

                v2 = self.arestas[a].v2.rotulo
                peso = int(self.arestas[a].peso)
                T = P[vertice] + peso

                if T < P[v2]:
                    P[v2] = T
                    A[v2] = vertice

        if P[destino] == float('inf'):
            return ([], float('inf'))

        caminho, i = [destino], destino
        while i != origem:
            i = A[i]
            caminho.append(i)

        return (caminho[::-1], P[destino])