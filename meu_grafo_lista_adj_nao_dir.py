from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        conjunto = set() # {X-Z, X-W, ...}

        # arestas existentes = {} ou [] | {{(A, A)}, {(A, B)}, ...} guarda set para verificação otimizada
        total = {frozenset((self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo)) for a in self.arestas}

        # pares possíveis
        for i in range(len(self.vertices)): # i| 0 -> n
            for j in range(i + 1, len(self.vertices)):  # j| ++i -> n
                v1 = self.vertices[i].rotulo
                v2 = self.vertices[j].rotulo
                if frozenset((v1, v2)) not in total: # {(v1, v2)} in {{(A, A)}, {(A, B)}, ...}
                    conjunto.add(f"{v1}-{v2}")
        return conjunto

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        return any(self.arestas[a].v1 == self.arestas[a].v2 for a in self.arestas)

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                grau += 1
            if self.arestas[a].v2.rotulo == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in self.arestas:
            for j in self.arestas:
                if i != j and {self.arestas[i].v1.rotulo, self.arestas[i].v2.rotulo} == {self.arestas[j].v1.rotulo, self.arestas[j].v2.rotulo}:
                    return True
        return False

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
        vna = self.vertices_nao_adjacentes()
        return False if (self.ha_laco() or len(vna) != 0) else True

    def dfs(self, V):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        def aux(Grafo, Vertice, verticesVisitados):
            for aresta in sorted(self.arestas_sobre_vertice(Vertice)):
                novoVertice = self.arestas[aresta].v1.rotulo if self.arestas[aresta].v1.rotulo != Vertice else self.arestas[aresta].v2.rotulo

                if aresta not in Grafo.arestas and novoVertice not in verticesVisitados:
                    verticesVisitados.append(novoVertice)
                    Grafo.adiciona_vertice(novoVertice)
                    Grafo.adiciona_aresta(aresta, Vertice, novoVertice)
                    Grafo = aux(Grafo, novoVertice, verticesVisitados)

            return Grafo

        arvoreDFS = MeuGrafo()
        arvoreDFS.adiciona_vertice(V)
        arvoreDFS = aux(arvoreDFS, V, [V])
        return arvoreDFS

    def bfs(self, V):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        def processo (v, g, lp, lv):
            lp.remove(v)
            lv.append(v)
            for a in sorted(self.arestas_sobre_vertice(v)):
                nv = self.arestas[a].v1.rotulo if (self.arestas[a].v1.rotulo != v) else self.arestas[a].v2.rotulo
                if nv not in lv and nv not in lp:
                    lp.append(nv)
                    g.adiciona_vertice(nv)
                    g.adiciona_aresta(a, v, nv)
            return g, lp, lv

        def aux(grafo, vertice):
            grafo, processando, visitados = processo(vertice, grafo, [vertice], [])

            while len(processando):
                novo_vertice = processando[0]
                if novo_vertice not in visitados:
                    grafo, processando, visitados = processo(novo_vertice, grafo, processando, visitados)
            return grafo

        grafo = MeuGrafo()
        grafo.adiciona_vertice(V)
        grafo = aux(grafo, V)
        return grafo