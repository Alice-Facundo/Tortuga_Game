# Tortuga - Salve o Oceano\!

## Descrição

"Tortuga" é um jogo 2D 8 bit em Python que visa conscientizar sobre a poluição dos oceanos de uma forma divertida e interativa. O jogador controla uma tartaruga em duas fases de jogo: primeiro, limpando o oceano do lixo enquanto desvia de perigos e, segundo, separando o lixo coletado para reciclagem.

## Fases do Jogo

### Fase 1: Limpando o Oceano

O objetivo é guiar a tartaruga para coletar 10 itens de lixo espalhados pelo oceano. No entanto, a tarefa não é tão simples, pois existem inimigos (navio, rede, arpão, pescador e anzol) que perseguem a tartaruga. Se um inimigo tocar na tartaruga, o jogo acaba.

### Fase 2: Reciclagem

Depois de coletar todo o lixo, o jogador avança para a segunda fase. Aqui, o desafio é arrastar cada item de lixo para a sua respectiva lixeira de reciclagem (Metal, Plástico, Vidro, Papel, Orgânico e Não reciclável) antes que o tempo de 60 segundos se esgote.

## Como Jogar

### Controles (Fase 1)

  * **Seta para Cima:** Mover para frente
  * **Seta para a Esquerda:** Virar à esquerda
  * **Seta para a Direita:** Virar à direita
  * **Q:** Sair do jogo

### Interação (Fase 2)

  * Clique no lixo que deseja mover.
  * Clique na lixeira correta para descartá-lo.

## Instalação e Execução

**Pré-requisitos:**

  * Python 3.x
  * As seguintes bibliotecas Python:
      * `turtle`
      * `random`
      * `winsound`
      * `os`
      * `tkinter`
      * `time`

**Instruções:**

1.  **Verifique os caminhos dos arquivos:**
    O jogo utiliza arquivos de imagem e som locais. É crucial que os caminhos para esses arquivos no código (`.py`) correspondam à sua localização no seu sistema. O código-fonte faz referência a um diretório `D:\`. Se a sua pasta de projeto estiver em outro local, você precisará atualizar esses caminhos.
2.  **Execute o jogo:**
    ```bash
    python "TORTUGA - VERSÃO FINAL.py"
    ```

## Objetivo Educacional

O jogo foi desenvolvido como uma ferramenta educativa para ensinar crianças e jovens sobre a importância da preservação dos oceanos e da reciclagem do lixo, mostrando de forma lúdica os perigos que a poluição representa para a vida marinha.
