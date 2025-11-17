import os
import pandas as pd

#  Função auxiliar para combinar múltiplas colunas
def _combine_cols(df: pd.DataFrame, candidates, new_name: str) -> pd.DataFrame:
    cols = [c for c in candidates if c in df.columns]
    if not cols:
        df[new_name] = pd.NA
    else:
        df[new_name] = df[cols].bfill(axis=1).iloc[:, 0]
    return df


# Função principal para carregar e padronizar o dataset
def load_happiness_data() -> pd.DataFrame:
    # Define diretório base relativo ao arquivo atual
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "dataset.csv")

    # Carrega o CSV original
    df = pd.read_csv(csv_path)


    # Padronização das colunas principais
    df = _combine_cols(df, ["Country", "Country or region"], "country") # Nome do país
    df = _combine_cols(df, ["Score", "Happiness Score", "Happiness.Score"], "happiness_score") # Score de felicidade
    # PIB per capita
    df = _combine_cols(
        df,
        ["Economy (GDP per Capita)", "Economy..GDP.per.Capita.", "GDP per capita"],
        "gdp"
    ) 
    df = _combine_cols(df, ["Family", "Social support"], "social_support") # Apoio social
    # Expectativa de vida
    df = _combine_cols(
        df,
        ["Health (Life Expectancy)", "Health..Life.Expectancy.", "Healthy life expectancy"],
        "health"
    )
    df = _combine_cols(df, ["Freedom", "Freedom to make life choices"], "freedom") # Liberdade
    df = _combine_cols(df, ["Generosity"], "generosity") # Generosidade
    # Corrupção/Confiança no governo
    df = _combine_cols(
        df,
        ["Trust (Government Corruption)", "Trust..Government.Corruption.", "Perceptions of corruption"],
        "corruption"
    )
    # Região
    df = _combine_cols(df, ["Region"], "region")

     # Convertendo ano para inteiro
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)

    # Remove linhas sem país ou sem score
    df = df.dropna(subset=["country", "happiness_score"])

    # Retorna o Dataframe
    return df
