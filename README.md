# 🌍 Felicidade Mundial: Dashboard Interativo com Streamlit ⭐

Este projeto consiste em um dashboard interativo **desenvolvido com Streamlit**, cujo objetivo é explorar visualmente dados associados ao World Happiness Report. 
A aplicação permite analisar fatores que influenciam a felicidade global, comparar países ao longo do tempo e identificar padrões importantes com base em indicadores socioeconômicos.

## 🎯 Objetivo do Projeto
Criar uma ferramenta interativa que ajude na descoberta de padrões e relações entre indicadores de felicidade, como:
- Tendência global de felicidade ao longo dos anos;
- Evolução da felicidade ao longo dos anos;
- Média dos fatores no último ano disponível;
- Relação entre felicidade e PIB per capita;
- Felicidade em função de PIB e Apoio Social;
- Distribuição da felicidade em 2019.


## 📁 Estrutura do Projeto
```
📂 Trabalho-Dashboard/
│
├── 📁 __pycache__/
│   └── data_utils.cpython-313.pyc
│
├── 📁 data/
│   └── dataset.csv                  # Dataset principal utilizado no dashboard
│
├── 📁 pages/                        # Páginas da aplicação (multipage)
│   ├── 🌎_Comparar_Países.py        # Página 1: Comparação entre países ao longo do tempo
│   ├── 💛_Fatores_da_Felicidade.py   # Página 2: Análise dos fatores que influenciam a felicidade
│   ├── 📊_Visão_Geral.py            # Página 3: Análises e métricas gerais
├── 🏠_Home.py                        # Página principal da navegação
├── data_utils.py                    # Funções auxiliares (carregar dados, limpeza, etc.)
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação do projeto
```

## 🚀 Como Executar o Projeto

### 1️⃣ Instalar dependências:
```bash
pip install -r requirements.txt
```

### 2️⃣ Executar o dashboard localmente:
```bash
streamlit run 🏠_Home.py
```
ou execute:
```bash
python -m streamlit run 🏠_Home.py
```

## 📚 Dataset Utilizado
O conjunto de dados foi retirado do Kaggle, permitindo analisar fatores associados à felicidade global.
Fonte do dataset: [https://www.kaggle.com/datasets/unsdsn/world-happiness](https://www.kaggle.com/datasets/unsdsn/world-happiness)

---

Este trabalho foi desenvolvido para a disciplina de **Programação II** da **Escola Técnica Estadual Monteiro Lobato (CIMOL)**. Todos os direitos reservados.
