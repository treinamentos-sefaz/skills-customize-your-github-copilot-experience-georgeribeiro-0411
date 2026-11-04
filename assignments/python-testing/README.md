# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Aprenda a verificar automaticamente o comportamento de funções Python usando pytest. Você vai escrever testes claros, executá-los pela linha de comando e cobrir tanto resultados válidos quanto situações de erro.

## 📝 Tarefas

### 🛠️ Escreva seus primeiros testes

#### Descrição
Crie um módulo `temperature.py` com a função `celsius_to_fahrenheit(celsius)`, que converte uma temperatura em Celsius para Fahrenheit usando a fórmula `celsius * 9 / 5 + 32`. Em seguida, crie `test_temperature.py` e escreva testes automatizados para alguns valores conhecidos.

#### Requisitos
O programa concluído deve:

- Ter a função `celsius_to_fahrenheit(celsius)` em `temperature.py`.
- Ter pelo menos três testes em `test_temperature.py`, incluindo `0 °C` (que deve resultar em `32 °F`) e `100 °C` (que deve resultar em `212 °F`).
- Executar os testes com `python -m pytest -q` e mostrar todos passando.

### 🛠️ Teste vários casos com parametrização

#### Descrição
Amplie os testes da conversão para verificar vários pares de entrada e resultado usando `@pytest.mark.parametrize`. Como a conversão pode produzir números decimais, use `pytest.approx` nas comparações quando necessário.

#### Requisitos
O programa concluído deve:

- Verificar pelo menos cinco valores de Celsius, incluindo um valor negativo e um valor decimal.
- Usar `@pytest.mark.parametrize` para executar o mesmo teste com diferentes valores.
- Usar `pytest.approx` para comparar resultados decimais sem depender de igualdade exata de ponto flutuante.

### 🛠️ Verifique situações inválidas

#### Descrição
Adicione a função `average_temperature(temperatures)` em `temperature.py`, que retorna a média de uma lista de temperaturas. Defina que uma lista vazia não pode ser calculada e deve gerar `ValueError`. Escreva testes que confirmem os resultados válidos e esse comportamento de erro.

#### Requisitos
O programa concluído deve:

- Retornar a média correta para uma lista com duas ou mais temperaturas.
- Gerar `ValueError` ao receber uma lista vazia.
- Usar `pytest.raises(ValueError)` para testar a exceção esperada.
- Executar novamente `python -m pytest -q` e confirmar que todos os testes passam.
