import streamlit as st
import plotly.express as px
from data_utils import load_happiness_data

# Configuração básica da página
st.set_page_config( 
    page_title="Felicidade Mundial",
    page_icon="😊",
    layout="wide"
)

# Armazenando a data em cache
@st.cache_data
def get_data():
    return load_happiness_data()

df = get_data()

st.title("📊 Felicidade Mundial (2015–2019)") # Título

# Informações em md
st.markdown("""
### 🎯 Objetivo do dashboard
Este dashboard foi criado para **explorar o Relatório Mundial de Felicidade (World Happiness Report)** entre os anos de **2015 e 2019**, permitindo identificar **tendências, padrões e relações** entre:
- nível de felicidade dos países;
- fatores como **PIB per capita**, **apoio social**, **saúde**, **liberdade**, **generosidade** e **corrupção**.

---

### 🧭 Como navegar entre as seções
Use o **menu lateral esquerdo** do Streamlit:
- Esta página inicial mostra uma visão geral do dataset e da felicidade média global por ano;
- As demais páginas (no menu *Pages*) trazem:
  - **Visão Geral**: distribuição da felicidade e top países;
  - **Fatores da Felicidade**: relação entre felicidade e outros indicadores;
  - **Comparar Países**: evolução da felicidade ao longo dos anos por país.

---

### 🎚️ Como os filtros influenciam os dados
Os filtros presentes nas páginas (como **ano**, **países** ou **indicadores**) alteram **diretamente os gráficos e tabelas**, permitindo:
- focar em um ano específico;
- comparar países entre si;
- analisar o impacto de diferentes fatores na felicidade.
""")

st.markdown("---")

# Métricas gerais em colunas
col1, col2, col3 = st.columns(3)

# Exibe um card com o número total de países distintos presentes no dataframe
with col1:
    st.metric("🌍 Número de países distintos", df["country"].nunique())

# Exibe o intervalo de anos presentes no dataset (mínimo e máximo)
with col2:
    st.metric("📅 Período analisado", f"{df['year'].min()} - {df['year'].max()}")

# Exibe o score médio global de felicidade (média geral de todos os países e anos)
with col3:
    st.metric("😊 Score médio global de felicidade", f"{df['happiness_score'].mean():.2f}")

# Título da seção
st.markdown("## 📈 Tendência global de felicidade ao longo dos anos")

# Agrupa os dados por ano e calcula a média de felicidade para cada ano
avg_year = df.groupby("year")["happiness_score"].mean().reset_index()

# Cria um gráfico de linha mostrando a evolução da felicidade média por ano
fig_line = px.line(
    avg_year,
    x="year",
    y="happiness_score",
    markers=True, # Mostra pontos no gráfico
    labels={"year": "Ano", "happiness_score": "Score médio de felicidade"},
    title="Felicidade média global por ano"
)
# Exibe o gráfico no Streamlit
st.plotly_chart(fig_line, use_container_width=True)

# Título da seção
st.markdown("## 🏆 Top 10 países no ano selecionado")

# Cria uma lista com todos os anos disponíveis, ordenados
anos_disponiveis = sorted(df["year"].unique())
# Selecionar ano
ano_selecionado = st.selectbox("Selecione o ano:", anos_disponiveis, index=len(anos_disponiveis)-1)

# Filtra o dataframe pelo ano escolhido e pega os 10 países com maior score
df_ano = df[df["year"] == ano_selecionado].sort_values(
    "happiness_score", ascending=False
).head(10)

# Cria gráfico de barras com os 10 países mais felizes no ano selecionado
fig_bar = px.bar(
    df_ano,
    x="country",
    y="happiness_score",
    labels={"country": "País", "happiness_score": "Score de felicidade"},
    title=f"Top 10 países mais felizes em {ano_selecionado}"
)

# Exibe o gráfico de barras
st.plotly_chart(fig_bar, use_container_width=True)