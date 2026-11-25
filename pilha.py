class NoPilha:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Pilha:
    """Pilha LIFO usada para guardar o histórico de faixas tocadas."""
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, musica):
        novo = NoPilha(musica)
        novo.proximo = self.topo
        self.topo = novo
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None
        musica = self.topo.musica
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return musica

    def remover_codigo(self, codigo):
        """Remove ocorrências do código sem usar lista auxiliar."""
        auxiliar = Pilha()
        removida = False
        while not self.esta_vazia():
            musica = self.desempilhar()
            if musica.codigo == codigo:
                removida = True
            else:
                auxiliar.empilhar(musica)
        while not auxiliar.esta_vazia():
            self.empilhar(auxiliar.desempilhar())
        return removida

    def __iter__(self):
        atual = self.topo
        while atual is not None:
            yield atual.musica
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
