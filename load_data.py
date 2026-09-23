"""データ読み込みモジュール。

data/raw/ の CSV を読み込んで DataFrame を返す。
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """CSV ファイルを読み込んで DataFrame を返す。

    Parameters
    ----------
    path : str | Path
        読み込む CSV ファイルのパス。

    Returns
    -------
    pd.DataFrame
        読み込んだデータ。
    """
    df = pd.read_csv(path)
    return df
