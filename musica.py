class Musica:
    def __init__(self, codigo, titulo, artista, album, duracao):
        self.codigo = codigo
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    def __str__(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return (f"[{self.codigo}] {self.titulo} - {self.artista} "
                f"({minutos}:{segundos:02d}) | Álbum: {self.album}")
