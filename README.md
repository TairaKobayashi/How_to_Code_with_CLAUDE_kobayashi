# sample-analysis

Claude Code ハンズオン用の最小解析プロジェクトです(生体情報システム研究室セミナー)。

被験者 60 名の心拍数・反応時間の架空データを群(A/B/C)ごとに集計します。
データには**意図的に欠損値**が含まれています(ハンズオン②で処理を追加します)。

## 構成

```
load_data.py                 # CSV 読み込み
stats.py                     # 群ごとの集計 → results/summary.csv
tests/test_load.py           # pytest
data/raw/subjects.csv        # 生データ(読み取り専用・変更禁止)
results/                     # 出力先(summary.csv, figures/)
references/style.mplstyle    # 論文投稿用の図スタイル(ハンズオン③で使用)
```

> **Note:** `references/style.mplstyle` は本ハンズオンの都合でリポジトリ直下に
> 置いています。実際の研究室運用では Skill と一緒に
> `.claude/skills/plot-style/references/` 配下に置くのが推奨です。

## セットアップと実行

### venv + pip を使う場合(推奨)

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e . pytest ruff   # 依存は pyproject.toml から導入される

pytest                  # テスト
python stats.py         # 集計を実行 → results/summary.csv
```

### uv を使う場合

```bash
uv sync                 # 依存の導入(.venv が自動作成される)
uv run pytest           # テスト
uv run python stats.py  # 集計を実行 → results/summary.csv
```

### conda を使う場合

```bash
conda create -n sample-analysis python=3.12 -y
conda activate sample-analysis
pip install -e . pytest ruff   # 依存は pyproject.toml から導入される

pytest                  # テスト
python stats.py         # 集計を実行 → results/summary.csv
```

## ルール

- `data/raw/` は読み取り専用。上書き・変更しない
- 図は `results/figures/` に保存する
