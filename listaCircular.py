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
        return self.inicio is None        return self.inicio is None

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