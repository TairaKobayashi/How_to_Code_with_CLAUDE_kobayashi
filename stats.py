"""集計モジュール。

群ごとの平均・標準偏差を計算し、results/summary.csv に保存する。
"""

from pathlib import Path

import pandas as pd

from load_data import load_csv


def summarize_by_group(df: pd.DataFrame, value_col: str = "heart_rate") -> pd.DataFrame:
    """group 列ごとに指定列の平均・SD・件数を集計する。

    Parameters
    ----------
    df : pd.DataFrame
        subject_id, group, および value_col を含むデータ。
    value_col : str
        集計する数値列の名前。

    Returns
    -------
    pd.DataFrame
        group, mean, sd, n の 4 列を持つ集計表。
    """
    summary = (
        df.groupby("group")[value_col]
        .agg(mean="mean", sd="std", n="count")
        .round(2)
        .reset_index()
    )
    return summary


def main() -> None:
    """data/raw/subjects.csv を集計して results/summary.csv に保存する。"""
    df = load_csv(Path("data/raw/subjects.csv"))
    summary = summarize_by_group(df)
    out = Path("results/summary.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out, index=False)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
