import streamlit as st
import plotly.express as px
from data_utils import load_happiness_data

# Configuração básica da página
st.set_page_config( 
    page_title="Visão Geral", 
    layout="wide"
)

# Armazenando a data em cache
@st.cache_data
def get_data():
    return load_happiness_data()

# Carrega o Dataframe
df = get_data()

# Título da página
st.title("📈 Visão Geral da Felicidade")

# Barra de filtro
st.sidebar.header("Filtros - Visão Geral")

# Lista ordenada de anos disponíveis
anos = sorted(df["year"].unique())

# Seleção para ano de análise (por padrão seleciona o último ano)
ano_escolhido = st.sidebar.selectbox("Selecione o ano", anos, index=len(anos)-1)

# Filtra o dataframe pelo ano selecionado
df_ano = df[df["year"] == ano_escolhido]

# Título da seção
st.markdown(f"### Distribuição da felicidade em **{ano_escolhido}**")

# Duas abas de análise
tab1, tab2 = st.tabs(["📊 Distribuição", "🏅 Top 10 Países"])

# Distribuindo as abas
with tab1:
    # Dividindo a tela em duas colunas
    col1, col2 = st.columns(2)

    # Gráfico dos scores no ano selecionado
    with col1:
        fig_hist = px.histogram(
            df_ano,
            x="happiness_score",
            nbins=20, # número de barras
            labels={"happiness_score": "Score de felicidade"},
            title=f"Histograma dos scores de felicidade ({ano_escolhido})"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    # Valores de todos os anos para comparar a evolução
    with col2:
        fig_box = px.box(
            df,
            x="year",
            y="happiness_score",
            labels={"year": "Ano", "happiness_score": "Score de felicidade"},
            title="Distribuição dos scores por ano"
        )
        st.plotly_chart(fig_box, use_container_width=True)
    
with tab2:
    # Ordena os países por score de felicidade e pega os 10 maiores
    df_top10 = df_ano.sort_values("happiness_score", ascending=False).head(10)

    # Gráfico de barras com os 10 países mais felizes
    fig_top10 = px.bar(
        df_top10,
        x="country",
        y="happiness_score",
        labels={"country": "País", "happiness_score": "Score de felicidade"},
        title=f"Top 10 países em {ano_escolhido}"
    )
    st.plotly_chart(fig_top10, use_container_width=True)

    # Exibe os dados em tabela, como país
    st.dataframe(
        df_top10[["country", "happiness_score", "gdp", "social_support", "health"]]
        .reset_index(drop=True)
    )