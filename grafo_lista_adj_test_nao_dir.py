import unittest
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(['J', 'C', 'E', 'P']).arestas(True).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(1).build()

        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()

        # Árvore DFS do gráfo da Paraíba começando do vértice C
        def criaGrafo (Vertice):
            grafo = MeuGrafo()

            for v in "JCEPMTZ":
                grafo.adiciona_vertice(v)

            return grafo

        def GrafoDFS (Vertice):
            grafo = criaGrafo(Vertice)
            dic = {
                'J': [('a1', 'J', 'C'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a8', 'T', 'M'), ('a9', 'T', 'Z')],
                'C': [('a1', 'C', 'J'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a8', 'T', 'M'), ('a9', 'T', 'Z')],
                'E': [('a2', 'E', 'C'), ('a1', 'C', 'J'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a8', 'T', 'M'), ('a9', 'T', 'Z')],
                'P': [('a4', 'P', 'C'), ('a1', 'C', 'J'), ('a2', 'C', 'E'), ('a6', 'C', 'T'), ('a8', 'T', 'M'), ('a9', 'T', 'Z')],
                'M': [('a7', 'M', 'C'), ('a1', 'C', 'J'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a9', 'T', 'Z')],
                'T': [('a6', 'T', 'C'), ('a1', 'C', 'J'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a7', 'C', 'M'), ('a9', 'T', 'Z')],
                'Z': [('a9', 'Z', 'T'), ('a6', 'T', 'C'), ('a1', 'C', 'J'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a7', 'C', 'M')],
            }

            for R, v1, v2 in dic[Vertice]:
                grafo.adiciona_aresta(R, v1, v2)

            return grafo
        def GrafoBFS (Vertice):
            grafo = criaGrafo(Vertice)
            dic = {
 #               'J': [('a1', 'J', 'C'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a7', 'C', 'M'), ('a9', 'T', 'Z')],
                'J': [('a1', 'J', 'C'), ('a2', 'C', 'E'), ('a4', 'C', 'P'), ('a6', 'C', 'T'), ('a7', 'C', 'M'), ('a9', 'T', 'Z')],
                "C": [("a1", "C", "J"), ("a2", "C", "E"), ("a4", "C", "P"), ("a6", "C", "T"), ("a7", "C", "M"), ("a9", "T", "Z")],
                "E": [("a2", "E", "C"), ("a1", "C", "J"), ("a4", "C", "P"), ("a6", "C", "T"), ("a7", "C", "M"), ("a9", "T", "Z")],
                "P": [("a4", "P", "C"), ("a1", "C", "J"), ("a2", "C", "E"), ("a6", "C", "T"), ("a7", "C", "M"), ("a9", "T", "Z")],
                "M": [("a7", "M", "C"), ("a8", "M", "T"), ("a1", "C", "J"), ("a2", "C", "E"), ("a4", "C", "P"), ("a9", "T", "Z")],
                "T": [("a6", "T", "C"), ("a8", "T", "M"), ("a9", "T", "Z"), ("a1", "C", "J"), ("a2", "C", "E"), ("a4", "C", "P")],
                "Z": [("a9", "Z", "T"), ("a6", "T", "C"), ("a8", "T", "M"), ("a1", "C", "J"), ("a2", "C", "E"), ("a4", "C", "P")],
            }

            for R, v1, v2 in dic[Vertice]:
                grafo.adiciona_aresta(R, v1, v2)

            return grafo

        self.g_J_dfs = GrafoDFS('J')
        self.g_C_dfs = GrafoDFS('C')
        self.g_E_dfs = GrafoDFS('E')
        self.g_P_dfs = GrafoDFS('P')
        self.g_M_dfs = GrafoDFS('M')
        self.g_T_dfs = GrafoDFS('T')
        self.g_Z_dfs = GrafoDFS('Z')

        self.g_J_bfs = GrafoBFS('J')
        self.g_C_bfs = GrafoBFS('C')
        self.g_E_bfs = GrafoBFS('E')
        self.g_P_bfs = GrafoBFS('P')
        self.g_M_bfs = GrafoBFS('M')
        self.g_T_bfs = GrafoBFS('T')
        self.g_Z_bfs = GrafoBFS('Z')


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs("J"), self.g_J_dfs)
        self.assertEqual(self.g_p.dfs("C"), self.g_C_dfs)
        self.assertEqual(self.g_p.dfs("E"), self.g_E_dfs)
        self.assertEqual(self.g_p.dfs("P"), self.g_P_dfs)
        self.assertEqual(self.g_p.dfs("M"), self.g_M_dfs)
        self.assertEqual(self.g_p.dfs("T"), self.g_T_dfs)
        self.assertEqual(self.g_p.dfs("Z"), self.g_Z_dfs)
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.dfs("A")

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs("J"), self.g_J_bfs)
        self.assertEqual(self.g_p.bfs("C"), self.g_C_bfs)
        self.assertEqual(self.g_p.bfs("E"), self.g_E_bfs)
        self.assertEqual(self.g_p.bfs("P"), self.g_P_bfs)
        self.assertEqual(self.g_p.bfs("M"), self.g_M_bfs)
        self.assertEqual(self.g_p.bfs("T"), self.g_T_bfs)
        self.assertEqual(self.g_p.bfs("Z"), self.g_Z_bfs)
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.bfs("A")