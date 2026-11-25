from musica import Musica
from lista_circular import ListaDuplamenteCircular
from fila import Fila
from pilha import Pilha
from tabela_hash import TabelaHash
from arvore_avl import ArvoreAVL


class PlayerMusica:
    def __init__(self):
        self.biblioteca = TabelaHash(211)  # código -> música
        self.playlist = ListaDuplamenteCircular()
        self.fila = Fila()
        self.historico = Pilha()
        self.avl = ArvoreAVL()
        self.atual = None

    def cadastrar_musica(self, codigo, titulo, artista, album, duracao):
        if self.biblioteca.buscar(codigo) is not None:
            return None
        musica = Musica(codigo, titulo, artista, album, duracao)
        self.biblioteca.inserir(codigo, musica)
        self.avl.inserir(musica)
        self.playlist.inserir_fim(musica)
        return musica

    def buscar_codigo(self, codigo):
        return self.biblioteca.buscar(codigo)

    def buscar_titulo(self, titulo):
        return self.avl.buscar(titulo)

    def remover_musica(self, codigo):
        musica = self.biblioteca.buscar(codigo)
        if musica is None:
            return None
        self.biblioteca.remover(codigo)
        self.avl.remover(musica.titulo, musica.codigo)
        self.playlist.remover(codigo)
        self.fila.remover_codigo(codigo)
        self.historico.remover_codigo(codigo)
        if self.atual is not None and self.atual.musica.codigo == codigo:
            self.atual = None
        return musica

    def enfileirar(self, codigo):
        musica = self.buscar_codigo(codigo)
        if musica is None:
            return False
        self.fila.enfileirar(musica)
        return True

    def proxima_musica(self):
        if self.fila.esta_vazia() and len(self.playlist) == 0:
            return None
        if self.atual is not None:
            self.historico.empilhar(self.atual.musica)
        if not self.fila.esta_vazia():
            musica = self.fila.desenfileirar()
            self.atual = self.playlist.buscar_no(musica.codigo)
            return musica
        self.atual = self.playlist.proximo_no(self.atual)
        return self.atual.musica

    def musica_anterior(self):
        anterior = self.historico.desempilhar()
        if anterior is not None:
            self.atual = self.playlist.buscar_no(anterior.codigo)
            return anterior
        if len(self.playlist) == 0:
            return None
        self.atual = self.playlist.anterior_no(self.atual)
        return self.atual.musica

    def musica_atual(self):
        return None if self.atual is None else self.atual.musica

    def executar_teste_carga(self, quantidade=3000):
        # Estruturas temporárias: o teste não altera a biblioteca do usuário.
        teste_avl = ArvoreAVL()
        teste_hash = TabelaHash(5003)
        for numero in range(quantidade):
            musica = Musica(numero, f"Faixa {numero:05d}", "Artista teste", "Álbum teste", 180)
            teste_hash.inserir(numero, musica)
            teste_avl.inserir(musica)
        return len(teste_hash), len(teste_avl), teste_avl.altura()