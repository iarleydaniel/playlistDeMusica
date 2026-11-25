from player import PlayerMusica


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def mostrar_musicas(musicas):
    encontrou = False
    for musica in musicas:
        print(musica)
        encontrou = True
    if not encontrou:
        print("Nenhuma música cadastrada.")


def menu():
    player = PlayerMusica()
    while True:
        print("\n========== PLAYER DE MÚSICA ==========")
        print("1 - Cadastrar música")
        print("2 - Listar biblioteca em ordem alfabética (AVL)")
        print("3 - Buscar música por código (Hash)")
        print("4 - Buscar música por título (AVL)")
        print("5 - Remover música")
        print("6 - Tocar próxima música")
        print("7 - Voltar música")
        print("8 - Adicionar música à fila 'tocar a seguir'")
        print("9 - Mostrar fila")
        print("10 - Mostrar playlist circular")
        print("11 - Mostrar histórico")
        print("12 - Executar teste de carga")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            codigo = ler_inteiro("Código: ", 1)
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            album = input("Álbum: ").strip()
            duracao = ler_inteiro("Duração em segundos: ", 1)
            if not titulo or not artista or not album:
                print("Título, artista e álbum não podem ficar vazios.")
            else:
                musica = player.cadastrar_musica(codigo, titulo, artista, album, duracao)
                print("Música cadastrada." if musica else "Já existe uma música com esse código.")

        elif opcao == "2":
            mostrar_musicas(player.avl.em_ordem())

        elif opcao == "3":
            codigo = ler_inteiro("Código da música: ", 1)
            musica = player.buscar_codigo(codigo)
            print(musica if musica else "Música não encontrada.")

        elif opcao == "4":
            titulo = input("Título: ").strip()
            musica = player.buscar_titulo(titulo)
            print(musica if musica else "Música não encontrada.")

        elif opcao == "5":
            codigo = ler_inteiro("Código da música a remover: ", 1)
            musica = player.remover_musica(codigo)
            print(f"Removida: {musica}" if musica else "Música não encontrada.")

        elif opcao == "6":
            musica = player.proxima_musica()
            print(f"Tocando agora: {musica}" if musica else "A biblioteca e a fila estão vazias.")

        elif opcao == "7":
            musica = player.musica_anterior()
            print(f"Voltando para: {musica}" if musica else "Não há música anterior.")

        elif opcao == "8":
            codigo = ler_inteiro("Código da música para a fila: ", 1)
            print("Adicionada à fila." if player.enfileirar(codigo) else "Código não encontrado.")

        elif opcao == "9":
            if len(player.fila) == 0:
                print("Fila vazia.")
            else:
                print("Fila de reprodução:")
                mostrar_musicas(player.fila)

        elif opcao == "10":
            if len(player.playlist) == 0:
                print("Playlist vazia.")
            else:
                print("Playlist (circular):")
                mostrar_musicas(player.playlist)

        elif opcao == "11":
            if len(player.historico) == 0:
                print("Histórico vazio.")
            else:
                print("Histórico (mais recente primeiro):")
                mostrar_musicas(player.historico)

        elif opcao == "12":
            quantidade = ler_inteiro("Quantidade de registros (ex.: 3000): ", 1)
            total_hash, total_avl, altura = player.executar_teste_carga(quantidade)
            print(f"Registros na Hash: {total_hash}")
            print(f"Registros na AVL: {total_avl}")
            print(f"Altura da AVL: {altura}")

        elif opcao == "0":
            print("Encerrando o player. Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
