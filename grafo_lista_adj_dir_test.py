import unittest
from meu_grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada
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
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb5.json', MeuGrafo())

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
            .arestas([ArestaDirecionada('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([ArestaDirecionada('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Algorítmo de Dijkstra
        self.g_r3 = MeuGrafo()
        for i in range(1, 34):
            self.g_r3.adiciona_vertice(f'v{i}')

        ad = (("a1", "v1", "v2", "1"), ("a2", "v1", "v3", "1"), ("a3", "v1", "v4", "2"),
              ("a4", "v2", "v5", "1"), ("a5", "v2", "v9", "2"),
              ("a6", "v3", "v7", "1"),
              ("a7", "v4", "v8", "1"),
              ("a8", "v5", "v6", "2"),
              ("a9", "v6", "v2", "1"), ("a10", "v6", "v10", "1"),
              ("a11", "v7", "v6", "1"), ("a12", "v7", "v11", "1"),
              ("a13", "v8", "v12", "1"), ("a14", "v8", "v7", "1"),
              ("a15", "v9", "v13", "2"),
              ("a16", "v10", "v9", "2"), ("a17", "v10", "v14", "2"),
              ("a18", "v11", "v15", "1"),
              ("a19", "v12", "v16", "2"),
              ("a20", "v13", "v17", "1"), ("a21", "v13", "v21", "4"),
              ("a22", "v14", "v20", "2"), ("a23", "v14", "v21", "2"), ("a24", "v14", "v18", "2"),
              ("a25", "v15", "v21", "3"),
              ("a26", "v16", "v18", "2"),
              ("a27", "v17", "v19", "1"),
              ("a28", "v19", "v22", "1"), ("a29", "v19", "v26", "2"),
              ("a30", "v20", "v23", "1"),
              ("a31", "v21", "v20", "2"), ("a32", "v21", "v25", "1"),
              ("a33", "v23", "v27", "1"), ("a34", "v23", "v24", "2"),
              ("a35", "v24", "v21", "1"),
              ("a36", "v25", "v28", "1"), ("a37", "v25", "v29", "1"),
              ("a38", "v26", "v30", "1"),
              ("a39", "v28", "v31", "1"),
              ("a40", "v30", "v31", "2"),
              ("a41", "v31", "v32", "1"), ("a42", "v31", "v33", "1"))

        for a, v1, v2, p in ad:
            self.g_r3.adiciona_aresta(a, v1, v2, p)

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
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
        self.assertEqual(self.g_p.grau_saida('J'), 1)
        self.assertEqual(self.g_p.grau_entrada('J'), 0)
        self.assertEqual(self.g_p.grau_saida('C'), 2)
        self.assertEqual(self.g_p.grau_entrada('C'), 5)
        self.assertEqual(self.g_p.grau_saida('E'), 0)
        self.assertEqual(self.g_p.grau_entrada('E'), 2)
        self.assertEqual(self.g_p.grau_saida('P'), 2)
        self.assertEqual(self.g_p.grau_entrada('P'), 0)
        self.assertEqual(self.g_p.grau_saida('M'), 2)
        self.assertEqual(self.g_p.grau_entrada('M'), 0)
        self.assertEqual(self.g_p.grau_saida('T'), 2)
        self.assertEqual(self.g_p.grau_entrada('T'), 1)
        self.assertEqual(self.g_p.grau_saida('Z'), 0)
        self.assertEqual(self.g_p.grau_entrada('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau_saida('G'), 5)

        self.assertEqual(self.g_d.grau_entrada('A'), 0)
        self.assertEqual(self.g_d.grau_saida('A'), 1)
        self.assertEqual(self.g_d.grau_entrada('C'), 0)
        self.assertEqual(self.g_d.grau_saida('C'), 0)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertEqual(self.g_d2.grau_entrada('A'), 0)
        self.assertNotEqual(self.g_d.grau_saida('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau_entrada('J'), 0)
        self.assertEqual(self.g_c.grau_saida('J'), 3)
        self.assertEqual(self.g_c.grau_entrada('C'), 1)
        self.assertEqual(self.g_c.grau_saida('C'), 2)
        self.assertEqual(self.g_c.grau_saida('E'), 1)
        self.assertEqual(self.g_c.grau_entrada('E'), 2)
        self.assertEqual(self.g_c.grau_saida('P'), 0)
        self.assertEqual(self.g_c.grau_entrada('P'), 3)

        # Com laço.
        self.assertEqual(self.g_l1.grau_saida('A'), 2)
        self.assertEqual(self.g_l1.grau_entrada('A'), 3)
        self.assertEqual(self.g_l2.grau_entrada('B'), 2)
        self.assertEqual(self.g_l2.grau_saida('B'), 2)
        self.assertEqual(self.g_l4.grau_entrada('D'), 1)
        self.assertEqual(self.g_l4.grau_saida('D'), 1)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas()) # X
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas()) # X
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas()) # X
        self.assertTrue(self.g_p3.ha_paralelas())
        self.assertFalse(self.g_p4.ha_paralelas())

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

    def test_dijkstra(self):
        testes = [(['v1', 'v2'], 1), (['v1', 'v2', 'v5'], 2), (['v1', 'v3', 'v7', 'v6'], 3),
                  (['v1', 'v3', 'v7', 'v6', 'v10'], 4), (['v1', 'v3', 'v7', 'v11'], 3),
                  (['v1', 'v3', 'v7', 'v6', 'v10', 'v14', 'v18'], 8), (['v1', 'v3', 'v7', 'v11', 'v15', 'v21'], 7),
                  (['v1', 'v3', 'v7', 'v6', 'v10', 'v14', 'v20', 'v23', 'v27'], 10),
                  (['v1', 'v3', 'v7', 'v11', 'v15', 'v21', 'v25', 'v28', 'v31'], 10),
                  (['v1', 'v3', 'v7', 'v11', 'v15', 'v21', 'v25', 'v28', 'v31', 'v33'], 11),
                  (['v10'], 0), ([], float('inf'))]
        self.assertEqual(self.g_r3.dijkstra('v1', 'v2'), testes[0])     # Caminho direto e curto
        self.assertEqual(self.g_r3.dijkstra('v1', 'v5'), testes[1])
        self.assertEqual(self.g_r3.dijkstra('v1', 'v6'), testes[2])     # Níveis de Profundidade
        self.assertEqual(self.g_r3.dijkstra('v1', 'v10'), testes[3])    # Múltiplas alternativas
        self.assertEqual(self.g_r3.dijkstra('v1', 'v11'), testes[4])
        self.assertEqual(self.g_r3.dijkstra('v1', 'v18'), testes[5])
        self.assertEqual(self.g_r3.dijkstra('v1', 'v21'), testes[6])    # Centro do grafo
        self.assertEqual(self.g_r3.dijkstra('v1', 'v27'), testes[7])    # Desvios Críticos
        self.assertEqual(self.g_r3.dijkstra('v1', 'v31'), testes[8])
        self.assertEqual(self.g_r3.dijkstra('v1', 'v33'), testes[9])    # Caminho longo até 33
        self.assertEqual(self.g_r3.dijkstra('v10', 'v10'), testes[10])  # Origem = Destino
        with self.assertRaises(VerticeInvalidoError):                                 # Origem não existe
            self.g_r3.dijkstra('v100', 'v1')
        with self.assertRaises(VerticeInvalidoError):                                 # Destino não existe
            self.g_r3.dijkstra('v1', 'v100')
        self.assertEqual(self.g_r3.dijkstra('v18', 'v1'), testes[11])   # Caminho impossível
