import streamlit as st
import plotly.express as px
from data_utils import load_happiness_data

# Configuração básica da página
st.set_page_config(
    page_title="Comparar Países", 
    layout="wide"
)

# Armazenando a data em cache
@st.cache_data
def get_data():
    return load_happiness_data()

# Carrega o Dataframe
df = get_data()

# Título da página
st.title("🌍 Comparar Países ao Longo do Tempo")

# Barra de filtro
st.sidebar.header("Filtros - Países")

# Lista de países
paises_disponiveis = sorted(df["country"].unique())

# Exibindo por padrão 3 países
paises_default = paises_disponiveis[:3]

# Campo para escolher um ou mais países
paises_selecionados = st.sidebar.multiselect(
    "Selecione os países que deseja comparar:",
    options=paises_disponiveis,
    default=paises_default
)

# Verifica se nenhum país for selecionado, exibindo aviso e interrompendo a execução
if not paises_selecionados:
    st.warning("Selecione pelo menos um país para comparar.")
    st.stop()

# Filtra o DataFrame apenas para os países escolhidos
df_paises = df[df["country"].isin(paises_selecionados)]

# Título da seção
st.markdown("### Evolução da felicidade ao longo dos anos")

# Cria gráfico de linha mostrando a evolução do score de felicidade por país
fig_line = px.line(
    df_paises.sort_values("year"), # Garante que os anos estão ordenados    
    x="year",
    y="happiness_score",
    color="country", # Cada país possui sua cor
    markers=True, # Adicionando marcadores nos pontos
    labels={"year": "Ano", "happiness_score": "Score de felicidade", "country": "País"},
    title="Evolução da felicidade por país"
)

# Exibindo o gráfico de linha
st.plotly_chart(fig_line, use_container_width=True)

# Título da seção
st.markdown("### Média dos fatores no último ano disponível")

# Descobre qual é o último ano que existe nos dados
ultimo_ano = df["year"].max()

# Filtra os dados apenas para o último ano e para os países selecionados
df_ultimo = df_paises[df_paises["year"] == ultimo_ano]

# Se não houver dados para esse ano, avisa o usuário
if df_ultimo.empty:
    st.info(f"Os países selecionados não possuem dados para {ultimo_ano}.")
else:
    # Lista de fatores que serão comparados
    fatores = ["gdp", "social_support", "health", "freedom", "generosity"]

    # Criando uma linha para cada combinação de país e fatores
    df_melt = df_ultimo.melt(
        id_vars=["country"], # Coluna que será mantida fixa
        value_vars=fatores,
        var_name="fator", # Nome da coluna com o nome do fator
        value_name="valor" # Nome da coluna com o valor do fator
    )

    # Dicionário para renomear o gráfico
    nomes_fatores_legenda = { 
        "gdp": "PIB per capita",
        "social_support": "Apoio social",
        "health": "Saúde",
        "freedom": "Liberdade",
        "generosity": "Generosidade",
    }

    # Cria uma coluna com os nomes para aparecer no gráfico
    df_melt["fator_legenda"] = df_melt["fator"].map(nomes_fatores_legenda)

    # Gráfico de barras agrupadas, comparando fatores por país
    fig_bar = px.bar(
        df_melt,
        x="fator_legenda", # Fatores
        y="valor", # Valor médio do fator
        color="country", # Cores por país
        barmode="group", # Barras agrupadas
        labels={"fator_legenda": "Fator", "valor": "Valor médio"}, # Renomeando no gráfico
        title=f"Comparação de fatores por país em {ultimo_ano}"
    )

# Exibe o gráfico de barras
st.plotly_chart(fig_bar, use_container_width=True)