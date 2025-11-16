import os
import pandas as pd

def _combine_cols(df: pd.DataFrame, candidates, new_name: str) -> pd.DataFrame:
    cols = [c for c in candidates if c in df.columns]
    if not cols:
        df[new_name] = pd.NA
    else:
        df[new_name] = df[cols].bfill(axis=1).iloc[:, 0]
    return df


def load_happiness_data() -> pd.DataFrame:
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "dataset.csv")

    df = pd.read_csv(csv_path)


    # Padronização das colunas principais
    df = _combine_cols(df, ["Country", "Country or region"], "country")
    df = _combine_cols(df, ["Score", "Happiness Score", "Happiness.Score"], "happiness_score")
    df = _combine_cols(
        df,
        ["Economy (GDP per Capita)", "Economy..GDP.per.Capita.", "GDP per capita"],
        "gdp"
    )
    df = _combine_cols(df, ["Family", "Social support"], "social_support")
    df = _combine_cols(
        df,
        ["Health (Life Expectancy)", "Health..Life.Expectancy.", "Healthy life expectancy"],
        "health"
    )
    df = _combine_cols(df, ["Freedom", "Freedom to make life choices"], "freedom")
    df = _combine_cols(df, ["Generosity"], "generosity")
    df = _combine_cols(
        df,
        ["Trust (Government Corruption)", "Trust..Government.Corruption.", "Perceptions of corruption"],
        "corruption"
    )
    df = _combine_cols(df, ["Region"], "region")

    if "year" in df.columns:
        df["year"] = df["year"].astype(int)

    # Remove linhas sem país ou sem score
    df = df.dropna(subset=["country", "happiness_score"])

    return df
