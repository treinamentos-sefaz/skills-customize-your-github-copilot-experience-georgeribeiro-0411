# 📘 Atividade: Games in Python

## 🎯 Objetivo

Praticar fundamentos de Python criando um jogo de terminal com entrada do usuario, loops, condicionais e manipulacao de strings.

## 📝 Tarefas

### 🛠️	Implementar o Jogo da Forca

#### Descrição
Implemente uma versao jogavel do jogo da Forca em Python, onde o jogador tenta adivinhar uma palavra secreta letra por letra.

#### Requisitos
O programa concluído deve:

- Definir uma lista com pelo menos 5 palavras possiveis.
- Escolher uma palavra aleatoriamente no inicio da partida.
- Exibir o progresso da palavra usando underscore para letras nao descobertas (exemplo: `_ _ _ _`).
- Permitir que o jogador digite um palpite de uma letra por rodada.
- Atualizar o estado do jogo apos cada palpite e mostrar as letras ja tentadas.
- Finalizar a partida com mensagem de vitoria quando todas as letras forem descobertas.
- Finalizar a partida com mensagem de derrota quando as tentativas acabarem, exibindo a palavra correta.


### 🛠️	Validar Entradas e Melhorar a Experiencia

#### Descrição
Adicione validacoes para tornar o jogo mais robusto e evitar entradas invalidas ou repetidas.

#### Requisitos
O programa concluído deve:

- Aceitar apenas uma letra por vez.
- Rejeitar entradas vazias, numeros ou simbolos.
- Avisar quando a letra ja tiver sido tentada e solicitar novo palpite.
- Exibir o numero de tentativas restantes apos cada rodada.
- Permitir jogar novamente ao fim da partida (opcional, mas recomendado).