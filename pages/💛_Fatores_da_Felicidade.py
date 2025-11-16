import streamlit as st
import plotly.express as px
from data_utils import load_happiness_data

# Configuração básica da página
st.set_page_config(
    page_title="Fatores da Felicidade", 
    layout="wide"
)

# Armazenando a data em cache
@st.cache_data
def get_data():
    return load_happiness_data()

# Carrega o Dataframe
df = get_data()

# Título da página
st.title("😊 Fatores Relacionados à Felicidade")

# Barra de filtro
st.sidebar.header("Filtros - Fatores")

# Cria uma lista com a opção dos anos disponíveis
anos = ["Todos"] + list(sorted(df["year"].unique()))
ano_filtro = st.sidebar.selectbox("Ano", anos, index=0)

# Se selecionar um ano específico, filtra
if ano_filtro != "Todos":
    df_filtrado = df[df["year"] == ano_filtro]
else:
    # Caso contrário, usa todos os dados
    df_filtrado = df.copy()

# Dicionário que mapeia fatores da felicidade
opcoes_fatores = {
    "PIB per capita": "gdp",
    "Apoio social": "social_support",
    "Saúde (expectativa de vida)": "health",
    "Liberdade": "freedom",
    "Generosidade": "generosity",
    "Corrupção (confiança inversa)": "corruption",
}

# Selecionando qual fator será comparado
fator_escolhido_legenda = st.sidebar.selectbox(
    "Selecione um fator para comparar com a felicidade:",
    list(opcoes_fatores.keys()),
)

# Pega o nome da coluna no dataframe a partir da escolha do usuário
fator_col = opcoes_fatores[fator_escolhido_legenda]

# Título da seção
st.markdown(f"### Relação entre felicidade e **{fator_escolhido_legenda}**")

# Cria o gráfico com o fator escolhido
fig_scatter = px.scatter(
    df_filtrado,
    x=fator_col, # Fator escolhido
    y="happiness_score", # Score de felicidade
    color="year", # Cor pra cada ano
    hover_name="country", # Mostra o país ao passar o mouse
    labels={
        fator_col: fator_escolhido_legenda,
        "happiness_score": "Score de felicidade",
        "year": "Ano"
    },
    title=f"Felicidade vs {fator_escolhido_legenda}",
    trendline="ols" # Linha de tendência
)

# Exibe o gráfico de dispersão
st.plotly_chart(fig_scatter, use_container_width=True)

# Título da seção
st.markdown("### Felicidade em função de PIB e Apoio Social")

fig_bubble = px.scatter(
    df_filtrado,
    x="gdp", # PIB per capita
    y="social_support", # Apoio social
    size="happiness_score", # Score da felicidade (tamanho da bolha)
    color="year", # Cor pra cada ano
    hover_name="country", # Nome do país
    # Dicionário para renomear o gráfico
    labels={
        "gdp": "PIB per capita",
        "social_support": "Apoio social",
        "happiness_score": "Score de felicidade"
    },
    title="Relação entre PIB, apoio social e felicidade"
)

# Exibe o gráfico de bolhas
st.plotly_chart(fig_bubble, use_container_width=True)