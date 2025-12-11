# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
- 
  1. Nome: Reginaldo Toshiaki Tanno

  2. Nome: Renato Silva e Lira

  3. Nome: Rogério Alves da Conceição
 

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?
<!-- Marque com X a opção correta -->
- [X] Sim
- [ ] Não

### 1.2 F1-Score obtido:
<!-- Copie o valor exibido ao final da execução -->
```
F1-Score: 0.4043
```

### 1.3 Cole aqui o output final do pipeline:
<!-- Execute: python main.py e copie a saída -->
```
PS C:\Users\lirar\Documents\MBA\Atividade_disciplina_1\trabalho_alunos> python main.py

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...

================================================================================
Extraído: 5000 linhas de data/clientes_campanha.csv
================================================================================
================================================================================
Exploração dos Dados
================================================================================
Shape: (5000, 8)

Tipos de Cada Coluna:

cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object


   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0
================================================================================

DISTRIBUIÇÃO DO TARGET EM NÚMEROS INTEIROS
--------------------------------------------------------------------------------
respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64

DISTRIBUIÇÃO DO TARGET EM PERCENTUAL
--------------------------------------------------------------------------------
proporção (percentual) de cada valor
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64
--------------------------------------------------------------------------------

[ETAPA 2/4] Validando dados...
C:\Users\lirar\Documents\MBA\Atividade_disciplina_1\venv\Lib\site-packages\pandera\_pandas_deprecated.py:146: FutureWarning: Importing pandas-specific classes and functions from the
top-level pandera module will be **removed in a future version of pandera**.
If you're using pandera to validate pandas objects, we highly recommend updating
your import:

```
# old import
import pandera as pa

# new import
import pandera.pandas as pa
```

If you're using pandera to validate objects from other compatible libraries
like pyspark or polars, see the supported libraries section of the documentation
for more information on how to import pandera:

https://pandera.readthedocs.io/en/stable/supported_libraries.html

To disable this warning, set the environment variable:

```
export DISABLE_PANDERA_IMPORT_WARNING=True
```

  warnings.warn(_future_warning, FutureWarning)
Validando dados...
✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...
Dados de treino: 4000 registros
Dados de teste: 1000 registros
Treinando modelo...
✅ Modelo treinado!
Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5550 (55.50%)
   Precision: 0.4951
   Recall:    0.3416
   F1-Score:  0.4043

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 404
   Falsos Positivos (FP):      154
   Falsos Negativos (FN):      291
   Verdadeiros Positivos (TP): 151

==================================================
🎯 F1-SCORE FINAL: 0.4043
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

📝 Anote o F1-Score no arquivo RESPOSTAS.md: 0.4043
```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?
<!-- Considere: F1 de 0.5 seria jogar moeda. Acima de 0.5 = melhor que aleatório. -->
Conforme o requisito acima, o modelo não apresenta bom resultado, pois o F1 ficou em 0.4043 abaixo do mínimo 0.5.


### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?
<!-- Dica: veja a proporção da variável target na exploração dos dados -->
O dataset é balanceado, com proporção de 56% para classe 0 e 44% para classe 1 (aproximadamente 1.27:1). Um dataset só é considerado desbalanceado quando a proporção ultrapassa 80/20 ou 4:1. Descobrimos isso através da análise da distribuição percentual do target exibida na etapa de exploração dos dados, onde o pipeline mostrou 56.06% de não-respondentes e 43.94% de respondentes.

DISTRIBUIÇÃO DO TARGET EM PERCENTUAL
--------------------------------------------------------------------------------
proporção (percentual) de cada valor
respondeu_campanha
0    0.5606
1    0.4394

Verificando o resultado de quem respondeu e não respondeu a campanha, percebemos que têm uma proporção não tão próxima um do outro.


### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?
<!-- Dica: pense no que aconteceria se o modelo previsse sempre 0 -->

Usamos F1-Score porque a Accuracy pode enganar: se o modelo previsse sempre "0" (classe majoritária), teria 56% de accuracy mas seria inútil. O F1-Score é a média harmônica entre Precision e Recall, penalizando tanto Falsos Positivos quanto Falsos Negativos. No contexto de campanhas de marketing, precisamos identificar quem responderá (Recall) e evitar desperdiçar recursos (Precision), e o F1-Score captura esse equilíbrio necessário.

Embora a Acurácia seja útil em dados balanceados, optamos pelo F1-Score porque ele oferece uma visão mais robusta do desempenho do modelo. A Acurácia pode ser enganosa se o modelo simplesmente 'chutar' a classe majoritária. O F1-Score penaliza tanto Falsos Positivos quanto Falsos Negativos, garantindo que o modelo realmente aprendeu a identificar o padrão, e não apenas a classe mais frequente.

---

## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:
<!-- Descreva cada validação que você adicionou -->
 # cliente_id — inteiro, não nulo, único
       
1. cliente_id: "cliente_id": Column(int, nullable=False, unique=True),
2. idade:  "idade": Column(int, Check.in_range(18, 80)),
3. renda_mensal: "renda_mensal": Column(float, Check.in_range(1000, 50000)),
4. score_credito:  "score_credito": Column(float, Check.in_range(300, 850)),
5. respondeu_campanha: "respondeu_campanha": Column(int, Check.isin([0, 1])),

### 3.2 Por que validar dados ANTES de treinar o modelo?
<!-- Pense no contexto de produção: o que aconteceria se dados inválidos entrassem no modelo? -->
Validar dados antes do treinamento é crítico porque previne falhas silenciosas em produção, garante qualidade seguindo o princípio "lixo entra, lixo sai", facilita debugging antecipado evitando desperdício de tempo computacional, e atende requisitos de auditoria. Exemplo prático: um score_credito de 1200 (inválido) passaria despercebido e faria o modelo aprender padrões incorretos, gerando previsões ruins em produção. A validação garante que apenas dados corretos entrem no pipeline.




---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):
<!-- Execute: git log --oneline e cole aqui -->
```
commit b665da80dcd60bb65b8ef80cf2ba7e2e9c0eaaf6 (HEAD -> master)
Author: RSL23RSL <lirarenato@yahoo.com.br>
Date:   Fri Dec 5 10:57:20 2025 -0300

    Implementação do terceiro módulo treinar modelo clientes_campanha.csv

commit 516db841b16a9d87d21d96720c6dfc97f34fa47a
Author: RSL23RSL <lirarenato@yahoo.com.br>
Date:   Fri Dec 5 10:53:31 2025 -0300

    Implementação do segundo módulo validar clientes_campanha.csv

commit ecfbc0d4962d16c12790fd8719c597c94162d6a7
Author: RSL23RSL <lirarenato@yahoo.com.br>
Date:   Fri Dec 5 10:40:37 2025 -0300

    Implementação do primeiro módulo carregar clientes_campanha.csv
(venv) PS C:\Users\lirar\Documents\MBA\Atividade_disciplina_1\trabalho_alunos> 
```

### 4.2 Por que mensagens de commit descritivas são importantes?
<!-- Pense: se outra pessoa olhar o histórico, vai entender o que foi feito? -->
As mensagens descritivas do GIT são fundamentais para outros desenvolvedores que acessarem as versões, bem como, o próprio desenvolvedor que as incluiu, permitindo que compreenda em que ponto aquela versão do código detém determinada alteração. Dessa forma caso necessite voltar alguma versão específica, por meio da mensagem descritiva é possível identificar a versão desejada.


---

## Parte 5: Reflexão (Opcional)

### 5.1 Qual foi a maior dificuldade do grupo?
O exercício foi bem explicado e com dicas que ajudaram a resolvê-lo. Em princípio é compreender os conceitos de features, target, como funciona o treinamento do modelo, como ele utiliza os números para alcançar o F1 a partir das variáveis fornecidas, que aqui foram poucas, mas para um modelo mais complexo, até conversão de letras em números é utilizada. 
Pela boa explicação do exercício não ocorreram dificuldades em sua resolução.


### 5.2 O que vocês fariam diferente se fossem refazer?

É possível existir outra forma de fazer o que foi proposto, porém, ainda foi cedo em termos de conhecimento mais aprofundado sobre como todo o processo se desenrola, o que com a aquisição de experiência novos insights surgirão para a resoluçao da mesma situação proposta de outra maneira.

---

**Data de entrega:** 11/12/2025
