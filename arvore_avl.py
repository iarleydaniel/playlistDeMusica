class NoAVL:
    def __init__(self, musica):
        self.musica = musica
        self.chave = (musica.titulo.casefold(), musica.codigo)
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.quantidade = 0

    def _altura(self, no):
        return 0 if no is None else no.altura

    def _atualizar(self, no):
        esquerda = self._altura(no.esquerda)
        direita = self._altura(no.direita)
        no.altura = (esquerda if esquerda > direita else direita) + 1

    def _fator(self, no):
        return 0 if no is None else self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, y):
        x = y.esquerda
        meio = x.direita
        x.direita = y
        y.esquerda = meio
        self._atualizar(y)
        self._atualizar(x)
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        meio = y.esquerda
        y.esquerda = x
        x.direita = meio
        self._atualizar(x)
        self._atualizar(y)
        return y

    def _balancear(self, no):
        if no is None:
            return None
        self._atualizar(no)
        fator = self._fator(no)
        if fator > 1:
            if self._fator(no.esquerda) < 0:
                no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        if fator < -1:
            if self._fator(no.direita) > 0:
                no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)
        return no

    def inserir(self, musica):
        self.raiz = self._inserir(self.raiz, musica)

    def _inserir(self, no, musica):
        if no is None:
            self.quantidade += 1
            return NoAVL(musica)
        chave = (musica.titulo.casefold(), musica.codigo)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, musica)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, musica)
        else:
            no.musica = musica
            return no
        return self._balancear(no)

    def buscar(self, titulo, codigo=None):
        chave_titulo = titulo.casefold()
        atual = self.raiz
        while atual is not None:
            if codigo is None:
                if chave_titulo == atual.chave[0]:
                    return atual.musica
                if chave_titulo < atual.chave[0]:
                    atual = atual.esquerda
                else:
                    atual = atual.direita
            else:
                chave = (chave_titulo, codigo)
                if chave == atual.chave:
                    return atual.musica
                atual = atual.esquerda if chave < atual.chave else atual.direita
        return None

    def remover(self, titulo, codigo):
        chave = (titulo.casefold(), codigo)
        antes = self.quantidade
        self.raiz = self._remover(self.raiz, chave)
        return self.quantidade < antes

    def _menor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                self.quantidade -= 1
                return no.direita
            if no.direita is None:
                self.quantidade -= 1
                return no.esquerda
            sucessor = self._menor_no(no.direita)
            no.musica = sucessor.musica
            no.chave = sucessor.chave
            no.direita = self._remover_sucessor(no.direita, sucessor.chave)
            self.quantidade -= 1
        return self._balancear(no)

    def _remover_sucessor(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esquerda = self._remover_sucessor(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_sucessor(no.direita, chave)
        else:
            return no.direita if no.esquerda is None else no.esquerda
        return self._balancear(no)

    def em_ordem(self):
        yield from self._percorrer(self.raiz)

    def _percorrer(self, no):
        if no is not None:
            yield from self._percorrer(no.esquerda)
            yield no.musica
            yield from self._percorrer(no.direita)

    def altura(self):
        return self._altura(self.raiz)

    def __len__(self):
        return self.quantidade
