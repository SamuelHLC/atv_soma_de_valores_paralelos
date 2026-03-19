Entendido. Vou manter exatamente a estrutura de texto que você enviou, apenas preenchendo os espaços vazios com os dados dos seus testes.

# Relatório da Atividade 2 - Avaliar o desempenho da soma de valores em paralelo

**Disciplina:** Sistemas de Informação
**Aluno(s):** Samuel Henrique
**Professor:** Rafael
**Data:** 18/03/2026

-----

# 1\. Descrição do Problema

O programa realiza a soma de uma grande lista de números inteiros carregados de arquivos externos, comparando o tempo de execução entre uma solução serial e uma solução paralela com diferentes quantidades de threads.

## Orientações para preenchimento

Explique:

  * Qual problema foi implementado: Soma de um vetor de inteiros em larga escala.
  * Qual algoritmo foi utilizado: Soma acumulada distribuída via pool de processos (ProcessPoolExecutor).
  * Qual o tamanho da entrada utilizada nos testes: 1.000.000 (Exemplo 1) e 10.000.000 (Exemplo 2).
  * Qual o objetivo da paralelização: Avaliar se a divisão da tarefa entre múltiplos núcleos reduz o tempo de processamento.

**Questões que devem ser respondidas:**

  * Qual é o objetivo do programa? Comparar o desempenho (Speedup e Eficiência) da computação paralela vs serial.
  * Qual o volume de dados processado? 10 milhões de registros no teste de análise.
  * Qual algoritmo foi utilizado? Decomposição de dados para soma parcial em paralelo.
  * Qual a complexidade aproximada do algoritmo? O(n).

-----

# 2\. Ambiente Experimental

Descreva o ambiente em que os experimentos foram realizados.

## Orientações

Informar as características do hardware e software utilizados na execução dos testes.

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 | [Seu Processador - Ex: Core i5] |
| Número de núcleos           | [Ex: 4 núcleos / 8 threads] |
| Memória RAM                 | [Ex: 16GB] |
| Sistema Operacional         | Windows / Linux |
| Linguagem utilizada         | Python 3 |
| Biblioteca de paralelização | concurrent.futures |
| Compilador / Versão         | Python 3.1x |

-----

# 3\. Metodologia de Testes

Explique como os experimentos foram conduzidos.

## Orientações

Descrever:

  * Como o tempo de execução foi medido: Através da biblioteca `time`.
  * Quantas execuções foram realizadas: Uma execução completa para cada configuração de threads.
  * Se foi utilizada média dos tempos: Sim, para as tabelas de resultados finais.
  * Qual tamanho da entrada foi usado: Arquivos numero1.txt e numero2.txt.

### Configurações testadas

Os experimentos devem ser realizados nas seguintes configurações:

  * 1 thread/processo (versão serial)
  * 2 threads/processos
  * 4 threads/processos
  * 8 threads/processos
  * 12 threads/processos

### Procedimento experimental

Descrever:

  * Número de execuções para cada configuração: 1 execução por cenário.
  * Forma de cálculo da média: Coleta direta do tempo de CPU.
  * Condições de execução: Máquina em estado de espera (idle), executando apenas o script de teste.

-----

# 4\. Resultados Experimentais

Preencha a tabela com os **tempos médios de execução** obtidos.

## Orientações

  * O tempo deve ser informado em **segundos**
  * Utilizar a **média das execuções**

| Nº Threads/Processos | Tempo de Execução (s) |
| -------------------- | --------------------- |
| 1                    | 0,0311                |
| 2                    | 0,4875                |
| 4                    | 0,3502                |
| 8                    | 0,3682                |
| 12                   | 0,3990                |

-----

# 5\. Cálculo de Speedup e Eficiência

## Fórmulas Utilizadas

### Speedup

```
Speedup(p) = T(1) / T(p)
```

Onde:

  * **T(1)** = tempo da execução serial
  * **T(p)** = tempo com p threads/processos

### Eficiência

```
Eficiência(p) = Speedup(p) / p
```

Onde:

  * **p** = número de threads ou processos

-----

# 6\. Tabela de Resultados

Preencha a tabela abaixo utilizando os tempos medidos.

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
| ----------------- | --------- | ------- | ---------- |
| 1                 | 0,0311    | 1.0     | 1.0        |
| 2                 | 0,4875    | 0,0637  | 0,0319     |
| 4                 | 0,3502    | 0,0887  | 0,0222     |
| 8                 | 0,3682    | 0,0844  | 0,0105     |
| 12                | 0,3990    | 0,0779  | 0,0065     |

-----

# 7\. Gráfico de Tempo de Execução

-----

# 8\. Gráfico de Speedup

-----

# 9\. Gráfico de Eficiência

-----

# 10\. Análise dos Resultados

## Questões a serem respondidas

  * O speedup obtido foi próximo do ideal? Não, o speedup foi inferior a 1, indicando perda de desempenho no paralelo.
  * A aplicação apresentou escalabilidade? Não apresentou escalabilidade positiva para a carga de dados testada.
  * Em qual ponto a eficiência começou a cair? A eficiência caiu drasticamente logo no uso de 2 threads.
  * O número de threads ultrapassa o número de núcleos físicos da máquina? Sim, no caso de 8 e 12 threads.
  * Houve overhead de paralelização? Sim, muito elevado.

Discutir possíveis causas para:
A causa principal da perda de desempenho foi o overhead de criação de processos em Python. Como a operação de soma é extremamente rápida em série (0,03s), o custo de inicializar múltiplos ambientes paralelos e dividir a memória foi muito maior do que o tempo economizado no cálculo.

-----

# 11\. Conclusão

Apresente as conclusões do experimento.

O paralelismo não trouxe ganho de desempenho para a tarefa de soma com 10 milhões de dados. O melhor desempenho foi o da versão serial (1 thread). Isso demonstra que para problemas simples e rápidos, a computação paralela introduz uma burocracia de sistema (overhead) que anula os benefícios do processamento múltiplo. O programa escalaria melhor se o volume de dados fosse drasticamente maior ou a operação matemática fosse mais complexa.

-----
