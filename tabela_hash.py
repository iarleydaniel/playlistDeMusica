class NoHash:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class TabelaHash:

    def __init__(self, capacidade=101):
        self.capacidade = capacidade
        self.buckets = [None] * capacidade 
        self.quantidade = 0

    def _funcao_hash(self, chave):
        texto = str(chave).casefold()
        valor = 0
        for caractere in texto:
            valor = (valor * 31 + ord(caractere)) % self.capacidade
        return valor

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        atual = self.buckets[indice]
        while atual is not None:
            if atual.chave == chave:
                atual.valor = valor
                return
            atual = atual.proximo
        novo = NoHash(chave, valor)
        novo.proximo = self.buckets[indice]
        self.buckets[indice] = novo
        self.quantidade += 1

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        atual = self.buckets[indice]
        while atual is not None:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, chave):
        indice = self._funcao_hash(chave)
        anterior = None
        atual = self.buckets[indice]
        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    self.buckets[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.quantidade -= 1
                return atual.valor
            anterior = atual
            atual = atual.proximo
        return None

    def __len__(self):
        return self.quantidade
