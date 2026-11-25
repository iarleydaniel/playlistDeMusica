class NoLista:
    def __init__(self, musica):
        self.musica = musica
        self.anterior = None
        self.proximo = None

class ListaDuplamenteCircular:
    """Playlist circular: cada nó conhece o anterior e o próximo."""
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def lista_vazia(self):
        return self.inicio is None

    def inserir_fim(self, musica):
        novo = NoLista(musica)
        if self.lista_vazia():
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior
            novo.proximo = self.inicio
            novo.anterior = ultimo
            ultimo.proximo = novo
            self.inicio.anterior = novo
        self.tamanho += 1
        return novo

    def buscar_no(self, codigo):
        if self.lista_vazia():
            return None
        atual = self.inicio
        while True:
            if atual.musica.codigo == codigo:
                return atual
            atual = atual.proximo
            if atual == self.inicio:
                break
        return None

    def remover(self, codigo):
        no = self.buscar_no(codigo)
        if no is None:
            return None
        if self.tamanho == 1:
            self.inicio = None
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior
            if no == self.inicio:
                self.inicio = no.proximo
        self.tamanho -= 1
        return no.musica

    def primeiro_no(self):
        return self.inicio

    def proximo_no(self, no_atual):
        if self.lista_vazia():
            return None
        if no_atual is None:
            return self.inicio
        return no_atual.proximo

    def anterior_no(self, no_atual):
        if self.lista_vazia():
            return None
        if no_atual is None:
            return self.inicio.anterior
        return no_atual.anterior

    def __iter__(self):
        if self.lista_vazia():
            return
        atual = self.inicio
        while True:
            yield atual.musica
            atual = atual.proximo
            if atual == self.inicio:
                break

    def __len__(self):
        return self.tamanho
