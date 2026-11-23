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