# Playlist de Música

Projeto acadêmico de Estruturas de Dados: um player de música em terminal para cadastrar, organizar, buscar e reproduzir músicas utilizando estruturas de dados implementadas em Python.

## Integrantes e tema

**Tema:** Sistema de gerenciamento de playlist / player de música.

**Integrantes:**
- Iarley Daniel Lima Procopio

## Funcionalidades

- Cadastrar músicas com código, título, artista, álbum e duração.
- Listar a biblioteca em ordem alfabética pelo título.
- Buscar músicas por código ou título.
- Remover músicas da biblioteca e das estruturas relacionadas.
- Avançar e voltar na playlist.
- Enfileirar músicas para tocar a seguir.
- Consultar a fila, a playlist circular e o histórico.
- Executar teste de carga e consultar a quantidade de registros e a altura da AVL.

## Requisitos

- Python 3.10 ou superior.
- Não há dependências externas; o projeto utiliza apenas a biblioteca padrão do Python.

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/iarleydaniel/playlistDeMusica.git
   ```

2. Entre na pasta:

   ```bash
   cd playlistDeMusica
   ```

3. Execute:

   ```bash
   python main.py
   ```

   No Windows, se necessário, use `py main.py`.

## Estruturas de dados utilizadas

### 1. Tabela hash — biblioteca e busca por código

Arquivo: `tabela_hash.py`

Armazena pares código–música. A função hash transforma a chave em um índice do vetor de buckets. As colisões são tratadas por encadeamento: cada bucket pode apontar para uma lista ligada de nós. A biblioteca do player utiliza capacidade 211.

**Justificativa:** como o código identifica cada música, a tabela hash permite localizar faixas diretamente pela chave,com custo esperado O(1) quando as chaves estão bem distribuídas. A capacidade 211 foi escolhida por ser um número primo, uma escolha comum em tabelas hash que pode favorecer a distribuição dos índices gerados pela função hash. O encadeamento permite tratar colisões e continuar armazenando músicas mesmo quando a quantidade de registros ultrapassa a capacidade inicial.

### 2. Árvore AVL — organização e busca por título

Arquivo: `arvore_avl.py`

É uma árvore binária de busca auto-balanceada. Cada nó armazena a música, uma chave composta pelo título normalizado com `casefold()` e pelo código, os filhos e a altura. Após inserções e remoções, as alturas são atualizadas e rotações simples ou duplas restauram o balanceamento. O percurso em ordem lista os títulos ordenadamente.

**Justificativa:**  foi escolhida para manter as músicas organizadas por título e permitir operações de busca, inserção e remoção com complexidade O(log n) no pior caso. O balanceamento automático evita que a árvore fique desproporcional, mantendo sua altura reduzida mesmo quando os dados são inseridos em ordem crescente ou decrescente.

### 3. Lista duplamente circular — playlist

Arquivo: `lista_circular.py`

Cada nó armazena referências para o próximo nó e para o nó anterior. O último nó aponta para o primeiro, enquanto o primeiro aponta para o último, formando uma estrutura circular. A lista mantém uma referência para o primeiro elemento e controla a quantidade de músicas armazenadas.

**Justificativa:** essa estrutura permite navegar continuamente entre as músicas, tanto para frente quanto para trás. A circularidade possibilita retornar à primeira música após a última faixa e, da mesma forma, voltar à última música ao retroceder a partir da primeira.

### 4. Fila encadeada — “tocar a seguir”

Arquivo: `fila.py`

A estrutura utiliza nós encadeados e mantém referências para o primeiro e o último elemento. A inserção de novas músicas acontece no final da fila, enquanto a remoção ocorre no início, seguindo o princípio FIFO (First In, First Out), em que o primeiro elemento a entrar é o primeiro a sair.

**Justificativa:** essa estrutura garante que as músicas sejam reproduzidas na mesma ordem em que foram adicionadas à fila. A manutenção das referências para o início e o fim permite realizar as operações de enfileiramento e desenfileiramento em O(1), sem a necessidade de percorrer todos os elementos.

### 5. Pilha encadeada — histórico

Arquivo: `pilha.py`

A estrutura utiliza nós encadeados e mantém uma referência para o topo da pilha. As operações de empilhamento e desempilhamento são realizadas nesse topo, seguindo o princípio LIFO (Last In, First Out), em que o último elemento inserido é o primeiro a ser removido.

**Justificativa:**  essa estrutura é adequada para armazenar o histórico de reprodução, pois, ao voltar para uma música anterior, a faixa tocada mais recentemente deve ser recuperada primeiro. A pilha representa naturalmente esse comportamento, permitindo realizar as operações de empilhar e desempilhar em O(1).

### 6. Classe Música e integração

Arquivos: `musica.py` e `player.py`

A classe Musica representa cada faixa cadastrada no sistema, armazenando seus atributos: código, título, artista, álbum e duração.

A classe PlayerMusica é responsável por integrar e gerenciar as cinco estruturas de dados do projeto: tabela hash, árvore AVL, lista duplamente circular, fila encadeada e pilha encadeada. Também mantém uma referência para a música atual e controla as operações do player.

Ao cadastrar uma música, o sistema a adiciona à tabela hash, à árvore AVL e à playlist circular. Ao remover uma faixa, atualiza as estruturas correspondentes, removendo também possíveis ocorrências na fila e no histórico.

**Justificativa:** a separação entre as classes facilita a organização do código. Enquanto Musica concentra os dados de cada faixa, PlayerMusica coordena as estruturas de dados e as funcionalidades do sistema, garantindo que elas trabalhem de forma integrada.

## Complexidade das operações

Considere **n** como a quantidade de elementos armazenados em cada estrutura. Na tabela hash, o pior caso ocorre quando várias chaves colidem no mesmo bucket, exigindo percorrer uma sequência de nós.

| Estrutura | Operação | Melhor caso | Pior caso |
|---|---|---:|---:|
| Tabela hash | Inserir | O(1) | O(n) |
| Tabela hash | Buscar | O(1) | O(n) |
| Tabela hash | Remover | O(1) | O(n) |
| Árvore AVL | Inserir | O(1) | O(log n) |
| Árvore AVL | Buscar | O(1) | O(log n) |
| Árvore AVL | Remover | O(1) | O(log n) |
| Árvore AVL | Percorrer em ordem | O(n) | O(n) |
| Lista duplamente circular | Inserir no fim | O(1) | O(1) |
| Lista duplamente circular | Buscar por código | O(1) | O(n) |
| Lista duplamente circular | Remover por código | O(1) | O(n) |
| Lista duplamente circular | Avançar/voltar um nó | O(1) | O(1) |
| Fila encadeada | Enfileirar | O(1) | O(1) |
| Fila encadeada | Desenfileirar | O(1) | O(1) |
| Fila encadeada | Consultar primeiro | O(1) | O(1) |
| Fila encadeada | Remover por código | O(1) | O(n) |
| Pilha encadeada | Empilhar | O(1) | O(1) |
| Pilha encadeada | Desempilhar | O(1) | O(1) |
| Pilha encadeada | Remover por código | O(n) | O(n) |

**Observações:**

- Na AVL, O(1) representa situações específicas de melhor caso, como encontrar um elemento na raiz ou inserir em uma árvore vazia. No pior caso, as operações de inserção, busca e remoção são O(log n), devido ao balanceamento da árvore.
- Na tabela hash, O(1) representa o melhor caso. O custo esperado é O(1) com uma boa distribuição das chaves, enquanto colisões podem elevar o custo para O(n) no pior caso.
- Na lista duplamente circular, inserir no fim é O(1) porque a referência para o último nó é acessada por meio de `inicio.anterior`. Buscar e remover por código podem exigir percorrer a lista, sendo O(n) no pior caso.
- Na fila, enfileirar e desenfileirar são O(1), pois a estrutura mantém referências para o início e o fim. Remover por código exige percorrer os elementos, sendo O(n) no pior caso.
- Na pilha, empilhar e desempilhar são O(1), pois ambas as operações acontecem no topo. Remover por código percorre os elementos e utiliza uma pilha auxiliar para preservar a ordem, sendo O(n).

## Testes realizados

Foram realizados testes manuais por meio do menu principal do sistema, verificando o funcionamento das estruturas de dados e sua integração com o player.

- **AVL:** cadastro de músicas em ordem aleatória, verificação da listagem alfabética e busca por título.
- **Tabela hash:** cadastro e busca de músicas por código, incluindo a consulta de códigos inexistentes.
- **Fila:** inclusão de músicas na fila e verificação da ordem de reprodução (FIFO).
- **Pilha:** avanço e retorno entre músicas, verificando o comportamento do histórico (LIFO).
- **Lista circular:** navegação entre músicas, verificando o retorno ao início da playlist e a navegação para a música anterior.

## Teste de carga da árvore AVL

O programa possui a opção **12 — Executar teste de carga**. Informe a quantidade desejada. O método `PlayerMusica.executar_teste_carga()` cria uma AVL e uma tabela hash temporárias, insere músicas sintéticas e retorna a quantidade armazenada em cada estrutura e a altura da AVL. O teste não altera a biblioteca do usuário.

### Resultados obtidos

| Registros inseridos | Registros na Hash | Registros na AVL | Altura da AVL |
|---:|---:|---:|---:|
| 1.000 | 1.000 | 1.000 | 10 |
| 5.000 | 5.000 | 5.000 | 13 |
| 10.000 | 10.000 | 10.000 | 14 |
| 20.000 | 20.000 | 20.000 | 15 |

**Ambiente em que esta análise foi executada:**  Windows 11, Python 3.13.5.

**Análise:**  todas as músicas foram inseridas tanto na tabela Hash quanto na árvore AVL, apresentando a mesma quantidade de registros nas duas estruturas. A altura da AVL passou de 10 níveis com 1.000 registros para 15 níveis com 20.000 registros. Esse crescimento lento é compatível com a complexidade de altura O(log n) esperada de uma árvore AVL.

## Divisão de tarefas

| Integrante | Responsabilidades |
| Iarley Daniel Lima Procopio (`@iarleydaniel`) | Desenvolvimento principal do projeto, incluindo implementação das estruturas de dados (árvore AVL, tabela hash, lista circular, fila e pilha), integração do player, desenvolvimento do menu, realização de ajustes, correções e testes. |

## Organização dos arquivos

```text
playlistDeMusica/
├── arvore_avl.py
├── fila.py
├── lista_circular.py
├── main.py
├── musica.py
├── pilha.py
├── player.py
├── tabela_hash.py
├── .gitignore
└── README.md
```
