"""load_data.load_csv の基本テスト。"""

from pathlib import Path

from load_data import load_csv

DATA = Path(__file__).parent.parent / "data" / "raw" / "subjects.csv"


def test_load_csv_shape() -> None:
    """60 名分・6 列のデータが読み込めること。"""
    df = load_csv(DATA)
    assert df.shape == (60, 6)
    assert list(df.columns) == [
        "subject_id",
        "group",
        "sex",
        "age",
        "heart_rate",
        "reaction_time_ms",
    ]
