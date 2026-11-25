class NoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    """Fila FIFO implementada com nós encadeados."""
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, musica):
        novo = NoFila(musica)
        if self.esta_vazia():
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        musica = self.inicio.musica
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        if self.inicio is None:
            self.fim = None
        return musica

    def primeiro(self):
        return None if self.esta_vazia() else self.inicio.musica

    def remover_codigo(self, codigo):
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.musica.codigo == codigo:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual == self.fim:
                    self.fim = anterior
                self.tamanho -= 1
                return atual.musica
            anterior = atual
            atual = atual.proximo
        return None

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.musica
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
